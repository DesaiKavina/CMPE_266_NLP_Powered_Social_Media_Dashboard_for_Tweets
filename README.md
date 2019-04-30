# CMPE_266 - Project Team 8

1. University Name: [San Jose State University](http://www.sjsu.edu/)
2. Course         : [Big Data Engineering and Analytics](http://info.sjsu.edu/web-dbgen/catalog/courses/CMPE266.html)
3. Professor      : [Sanjay Garje](https://www.linkedin.com/in/sanjaygarje/)
4. Students       : [Sayali Patil](https://www.linkedin.com/in/sayali-patil-7b041078/)
                    [Vagdevi Challa](https://github.com/vagdevichalla)

## Project Introduction :
Twitter is one of the eminent social media platform that gets a tremendous amounts of tweets everyday. This huge amount of information can be used for financial,government or social approaches by organizing and examining the tweets. Since the volume of data generated by Twitter is enormous, storage and processing of this data is a serious issue.

In order to extract useful information from data generated via twitter tweets, we used
various readily available cloud services from AWS. Services that are used in this project includes
Kinesis data fire hose, Amazon S3, AWS Lambda, AWS Translate, AWS Comprehend, Athena
and Amazon Quick sight. Following gives the overview of how tweets are analyzed to extract
useful information out of it.

1) In this project, we used Kinesis data fire hose to get real time data from twitter. In
order to extract real time data from twitter, Consumer key, Consumer secret key, access
token and access secret token is needed to connect to twitter. Once an app is created in
twitter, all these keys will be available and data can be extracted. Once the data is
extracted from twitter, it can be stored on various storage services like data stores, data
warehouses and data lakes. For this project, we used Amazon S3 to store the data generated from twitter.
2) Then, we used AWS Lambda that uses two fully managed services, AWS Translate
and AWS Comprehend to analyze tweets. These two services helped to perform NLP
(Natural language processing) on tweets.
3) Separate Kinesis data delivery streams within kinesis fire hose service is used in order to write back data to s3 bucket.
4) Once the enriched data is stored on S3, we used Athena to query the data that is
stored on S3.
5) Then,used Amazon quick sight to visualize analyzed data.

## Sample Demo Screenshots : 

## Pre-requisites Set Up :

Below is the list of reaourses to be configured  for this project :

  Amazon S3 <br/>
  Amazon Kinesis Data Firehose <br/>
  Amazon Athena <br/>
  Amazon QuickSight <br/>

