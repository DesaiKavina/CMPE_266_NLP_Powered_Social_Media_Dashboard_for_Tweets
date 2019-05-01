'use strict';

var config = require('./config');
var twitter_config = require('./twitter_reader_config.js');
var Twit = require('twit');
var util = require('util');
var logger = require('./util/logger');

function twitterStreamProducer(firehose) {
  var log = logger().getLogger('producer');
  var waitBetweenPutRecordsCallsInMilliseconds = config.waitBetweenPutRecordsCallsInMilliseconds;
  var T = new Twit(twitter_config.twitter)

  function _sendToFirehose() {

    var stream = T.stream('statuses/filter', { track: twitter_config.topics , language: twitter_config.languages });


    var records = [];
    var record = {};
    var recordParams = {};
    stream.on('tweet', function (tweet) {
                var tweetString = JSON.stringify(tweet)
                recordParams = {
                  DeliveryStreamName: twitter_config.kinesis_delivery,
                  Record: {
                    Data: tweetString +'\n'
                  }
                };
              firehose.putRecord(recordParams, function(err, data) {
                if (err) {
                  console.log(err);
                }
              });
        }
    );
  }


  return {
    run: function() {
      log.info(util.format('Configured wait between consecutive PutRecords call in milliseconds: %d',
          waitBetweenPutRecordsCallsInMilliseconds));
        _sendToFirehose();
      }
  }
}

module.exports = twitterStreamProducer;