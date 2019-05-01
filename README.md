# CMPE_266 - Project Team 8

1. University Name: [San Jose State University](http://www.sjsu.edu/)
2. Course         : [Big Data Engineering and Analytics](http://info.sjsu.edu/web-dbgen/catalog/courses/CMPE266.html)
3. Professor      : [Sanjay Garje](https://www.linkedin.com/in/sanjaygarje/)
4. Students       : [Sayali Patil](https://www.linkedin.com/in/sayali-patil-7b041078/) <br/>
		    [Vagdevi Challa](https://www.linkedin.com/in/vagdevi-challa-bbb46161/) <br/>
		    [Mohinish Daswani](https://www.linkedin.com/in/mohinish-daswani-0318a6110/) <br/>
		    [Kavina Desai](https://www.linkedin.com/in/kavina-desai)<br/>
		    [Sai Supraja Malla](https://www.linkedin.com/in/saisuprajamalla/) <br/>
        

	            

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
5) Then, used Amazon quick sight to visualize analyzed data.

## Sample Demo Screenshots : 

## Pre-requisites Set Up :

Below is the list of resources to be configured for this project:

  Amazon S3 <br/>
  Amazon Simple Storage Service (Amazon S3) is an object storage service offering scalability, data availability, security,    	 and performance. It is designed for 99.999999999% of durability, and storing the data for millions of applications for      
  organizations all around the world. <br/> Below are the steps to create S3 bucket : <br/> 
  	
	1. Open Amazon S3 console at https://console.aws.amazon.com/s3/.
	2. Choose Create bucket.
	3. Enter the bucket name and region where you want the bucket to reside. (here region is N. Virginia)
	4. Choose Create. 
	
	
 
  Amazon Kinesis Data Firehose <br/>
  Amazon Kinesis Data Firehose is used for reliably loading streaming data into data stores and analytics tools. It captures, 	transforms, and loads streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, Splunk and enables near   real-time analytics with existing business intelligence tools and dashboards. <br/>
  In this project, we are capturing real time Twitter data in Amazon Kinesis Data firehose for the analysis.<br/>
  
  
  Amazon Athena <br/>
  Amazon Athena is an interactive query service making it easy for analyzing data in Amazon S3 using standard SQL. Athena is     serverless, so there is no infrastructure to manage, and you pay only for the queries that you run. <br/>
  Amazon QuickSight <br/>
  Amazon QuickSight is a fully managed service that lets you easily create and publish interactive dashboards including ML     	 Insights. Dashboards can then be accessed from any device, and embedded into your applications, portals, and websites. <br/>
  

  Amazon IAM <br/>
  
  
  Amazon Lambda <br/>
  Amazon EC2 <br/>
  Amazon Elastic Compute Cloud (Amazon EC2) is a web service providing secure, resizable compute capacity in the cloud. It is 	designed to make web-scale cloud computing easier for developers. <br/>
  Below are the steps for creating AWS EC2 instance for this project : <br/>
  
  	Create VPC and subnets with below configuration :
	Select this option (to avoid charges to your account):
    	In "Specify the details of your NAT gateway" Section, Select "Use NAT Instance Instead".  
	
	    NAT Instance Type:          t2.micro
	    NAT Instance Keypair:       

	    CIDR block                  10.0.0.0/16 
	    Public Subnet:              10.193.10.0/24
 	
	Launch a new EC2 Instance into your new VPC as follows:

	T2 Micro Instance
	VPC: Twitter_Data
	Public Subnet
	Auto Assign Public IP
	Security Group: (create new) with ports 22 open
	Select Key Pair: 
	AWS Instance Name: Twitter_data

 

## How to run the project

**Step1** : Log in into the AWS console and go to the EC2 dashboard.

**Step2** : SSH into the created linux instance. After logging in the instance run the following command
```
node twitter_stream_producer_app.js
```
This command will start extracting data from the Twitter and put it into Amazon S3 through kinesis firehose. As the data comes in the S3 bucket, lambda function is triggered which fetches the twitter data, performs analysis on it and pushes back to the S3 bucket

**Step3** : Go to Athena dashboard and create external table in Athena. After creating the table, write SQL queries. The query output will be stored in a new S3 bucket.

**Step4** : Go to Amazon Quicksight console and create a new data set in it and choose the tables created in Amazon Athena. After that, run a query in the Quicksight console and you can see graphs generated from the results of the query.


