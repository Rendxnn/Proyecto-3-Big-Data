from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CovidDataProcessing").getOrCreate()

raw_s3_path = 's3://duque-uribe-rendon-p3/covid_data/'  # Zona raw
trusted_s3_path = 's3://duque-uribe-rendon-p3/covid_data_trusted/'  # Zona trusted

df_raw = spark.read.parquet(raw_s3_path)

df_filtered = df_raw.filter(df_raw.estado != "N/A") #Eliminado de todos los datos cuyo estado sea N/A

df_filtered.write.mode("overwrite").parquet(trusted_s3_path)

print(f"Datos filtrados guardados en S3 en {trusted_s3_path}")