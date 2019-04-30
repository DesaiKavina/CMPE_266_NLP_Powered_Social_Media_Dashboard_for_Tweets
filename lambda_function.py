import json
import boto3
import os
import urllib
import logging

def lambda_handler(event, context):
    
    print("Inside the lambda_handler function")
    sentimentStream = os.environ['SENTIMENT_STREAM']
    entityStream = os.environ['ENTITY_STREAM']
    s3 = boto3.client('s3')
    # print("\nEvent : \n",event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    print("Bucket name : ",bucket)
    key = event['Records'][0]['s3']['object']['key']
    # key = urllib.unquote(event.Records[0].s3.object.key.replace(/\+/g, ' '))
    print("Key : ",key)
    # bucket = 'twitter-data-analysis-template-tweetsbucket-148qppwe3ccpw'
    # key = 'raw/2019/04/26/20/Twitter-data-analysis-temp-IngestionFirehoseStream-DW0G1A8RBJTA-1-2019-04-26-20-37-02-b9f2cc79-007c-47ca-a167-8ac5d0e83075'
    try:
        data = s3.get_object(Bucket=bucket, Key=key)
        tweets = data['Body'].read().decode('utf-8')
        tweetArray = tweets.split('\n')
        for tweetline in tweetArray:
            if len(tweetline) > 0:
                tweet = json.loads(tweetline)
                comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
                firehose = boto3.client('firehose')
                
#############################################################################################################################
                
                tweet_sentiments = comprehend.detect_sentiment(Text=tweet['text'], LanguageCode='en')
                sentimentrecord = {
                    'Data' : json.dumps({
                        "tweetid": tweet['id'],
                        "text": tweet['text'],
                        "sentiment": tweet_sentiments['Sentiment'],
                        "sentimentPosScore": round( float(tweet_sentiments['SentimentScore']['Positive'] ), 3),
                        "sentimentNegScore": round( float(tweet_sentiments['SentimentScore']['Negative'] ), 3),
                        "sentimentNeuScore": round( float(tweet_sentiments['SentimentScore']['Neutral'] ), 3),
                        "sentimentMixedScore": round( float(tweet_sentiments['SentimentScore']['Mixed'] ), 3)   
                    }) + '\n'
                }
                response = firehose.put_record(DeliveryStreamName=sentimentStream, Record=sentimentrecord)
                print(" ------------ After firehose put record of sentiment data")
                
######################################################################################################################################                
                
                tweet_entities = comprehend.detect_entities(Text = tweet['text'], LanguageCode='en')
                for entity in tweet_entities['Entities']:
                    entityrecord = {
                        'Data' : json.dumps({
                            "tweetid": tweet['id'],
                            "entity": entity['Text'],
                            "type": entity['Type'],
                            "score": entity['Score']
                        }) + '\n'
                    }
                    firehose.put_record(DeliveryStreamName = entityStream, Record = entityrecord)
                print(" ______________ After firehose put record of entity data")
    except Exception as e:
        logging.error(e)
        raise e