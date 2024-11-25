from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, month, year

# Inicia la sesión Spark
spark = SparkSession.builder.appName("CovidAnalysis").getOrCreate()

# Carga de datos desde la zona trusted de S3
trusted_s3_path = "s3://duque-uribe-rendon-p3/covid_data_trusted/"
data = spark.read.parquet(trusted_s3_path)

# Ruta para guardar los resultados en la zona refined de S3
refined_s3_path = "s3://duque-uribe-rendon-p3/covid_data_refined/"

# 1. Distribución por ciudad y departamento
ciudad_departamento = data.groupBy("ciudad_municipio_nom", "departamento_nom").count()
ciudad_departamento.write.mode("overwrite").parquet(f"{refined_s3_path}/ciudad_departamento")

# 2. Distribución por género
genero = data.groupBy("sexo").count()
genero.write.mode("overwrite").parquet(f"{refined_s3_path}/genero")

# 3. Distribución por estado
estado = data.groupBy("estado").count()
estado.write.mode("overwrite").parquet(f"{refined_s3_path}/estado")

# 4. Análisis temporal - Casos por mes basado en fecha_inicio_sintomas
temporal = data.withColumn("mes", month(col("fecha_inicio_sintomas"))) \
               .withColumn("año", year(col("fecha_inicio_sintomas"))) \
               .groupBy("año", "mes").count()
temporal.write.mode("overwrite").parquet(f"{refined_s3_path}/temporal")

# 5. Distribución por tipo de recuperación
tipo_recuperacion = data.groupBy("tipo_recuperacion").count()
tipo_recuperacion.write.mode("overwrite").parquet(f"{refined_s3_path}/tipo_recuperacion")
