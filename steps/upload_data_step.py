from pyspark.sql import SparkSession
import requests


#Funcion para hacer peticion
def fetch_data(offset, size):
    uri = f'{covid_data_base_uri} select * limit {size} offset {offset}'
    
    response = requests.get(uri)  
    if response.status_code == 200: 
        return response.json()  
    else:
        print(f"Error fetching offset {offset}")  
        return None


#Funcion para traer un total de filas de datos de covid
def fetch_and_save_data(total_rows, size, s3_path):
    all_data = [] 

    for offset in range(0, total_rows, size):
        data = fetch_data(offset, size) 
        if data:
            all_data.extend(data) 

    if all_data:
        df = spark.createDataFrame(all_data)  
        df.write.mode("overwrite").parquet(s3_path)  
        print(f"All data saved to S3 at {s3_path}")
    else:
        print("No data to save")



spark = SparkSession.builder.appName("CovidDataProcessing").getOrCreate()
size = 20_000
total_rows = 100_000
covid_data_base_uri = 'https://www.datos.gov.co/api/id/gt2j-8ykr.json?$query='
s3_path = 's3://duque-uribe-rendon-p3/covid_data/'
fetch_and_save_data(total_rows, size, s3_path)