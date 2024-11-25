from pyspark.sql import SparkSession

# Inicia la sesión de Spark
spark = SparkSession.builder.appName("CovidDataProcessing").getOrCreate()

# Rutas de los datos en S3
raw_s3_path = 's3://duque-uribe-rendon-p3/covid_data/'  # Zona raw
trusted_s3_path = 's3://duque-uribe-rendon-p3/covid_data_trusted/'  # Zona trusted

# Carga los datos en formato Parquet desde la zona raw
df_raw = spark.read.parquet(raw_s3_path)

# Filtra los datos para eliminar los registros donde el estado sea "N/A"
df_filtered = df_raw.filter(df_raw.estado != "N/A")

# Guarda los datos filtrados en la zona trusted
df_filtered.write.mode("overwrite").parquet(trusted_s3_path)

print(f"Datos filtrados guardados en S3 en {trusted_s3_path}")
