#Extraction of Data From Sensors
This project is about extraction os data from sensors of a Wind Farm. In order to study the tools of the Aws. Three sensors was choose are they Power Factor, Temperature Battery and Hydraulic Pressure.
The objective is to create a flow of Extraction, Transform and Load.

##Tools used:
	- AWS Kinesis Data Stream;
	- AWS Kinesis Data Firehouse;
	- AWS S3;
	- AWS Glue Crawler;
	- AWS Glue Catalog;
	- AWS Glue Job;
	- AWS Athena;
	- Google Colab;
	
###1º Create the kinesis Data Stream:
	- This serves for colet the data from the sensors;
	
###2º Create the application who is simulate the data;
	- In order to generate the data, this applications was created in the Google Colab. Uses Python;
	- The files are in the PyApplication directory;
	- You need to complete the python application with your:
		- aws_access_key_id;
		- aws_secret_access_key;
		- region_name;
		- StreamName;
	
###3º Create a Bucket on S3;
	- This will keep the files generated from the application and the parquet files generated from the Job;
	
###4º Create a delivery flow on Kinesis Data Firehouse;
	- This flow will delivery the data from Data Streams to S3;
	
###5º Create  a Data Base on Glue Catalog;
	- You will need this for keep the data extracted;
	
###6º Create tables on Crawler from data that is in S3;
	- This will generate the tables for the Data Base from the S3 Data;
	
###7º Create a "DataLake" on the S3
	- This will make possible Athena consumes the data generated;
	
###8º Create a job for generation of parquet files;
	- This job will take the data from the Glue Catalog and transform in parquet files to the datalake on the S3;
	
###9º View the data on Athena;
	- The data from sensors are available for consult;
	
	
	
##Be careful this flow can generation costs;