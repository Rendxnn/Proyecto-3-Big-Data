# Proyecto 3: Tópicos de Telemática ST0263

## Estudiantes
- **Jaime Uribe**: jruribem@eafit.edu.com
- **Juan Pablo Duque**: jpduquep@eafit.edu.co
- **Samuel Rendon**: jpduquep@eafit.edu.co

## Profesor
- **Alvaro Enrique Ospina Sanjuan**: aeospinas@eafit.edu.co

## 1. Descripcion
El proyecto consta del despliegue de un cluster EMR en AWS para el proceso ETL de datos de contagios de Covid en colombia.

Se utilizaron Steps dentro del cluster para toda la manipulación de la información (extracción, tratamiendo y carga).

Los datos se obtuvieron del servicio web del Ministerio de Salud, por medio de la URL: https://www.datos.gov.co/api/id/gt2j-8ykr.json?$query=

Se realizaron varias consultas para obtener los datos crudos de 100.000 registros de contagios de Covid, los cuales fueron almacenados en la zona Raw del almacenamiento S3 de AWS.
Ver [step para la subida de datos](steps/upload_data_step.py)

Posteriormente, se realizó un filtrado y limpieza de la información para obtener únicamente informacion relevante, y se guardó la información resultante en la zona Trusted de S3.
Ver [step para la limpieza y filtrado de datos](steps/filter_and_clean_data_step.py)

Finalmente, se realizó un análisis de los datos para obtener información valiosa a partir de los datos limpiados y filtrados, que se almacenó en la zona Refined de S3.
Ver [step para el análisis de los datos](steps/data_analysis_step.py)


Tras haber realizado todo el proceso ETL de los datos del covid, se accedió a estos desde Athena en AWS.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Se cumplió con los requisitos de la actividad.


# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

### Lenguaje de programación: Python  -  PySpark

Se puede encontrar todo el código fuente de los steps desarrollados [aquí](steps/)

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

Cluster EMR de AWS con la siguiente configuracion:

Aplicaciones:

![image](https://github.com/user-attachments/assets/06724ca3-2f46-4824-9f5f-3de146ae6acf)


Máquinas usadas: m5.xlarge

![image](https://github.com/user-attachments/assets/89c3cd5c-e91c-4dc8-9429-a566a47d25f2)


Escalamiento y redes:

![image](https://github.com/user-attachments/assets/a2d7ded5-84de-4b81-885a-e20778e2b1a0)


Seguridad: kepair creado

![image](https://github.com/user-attachments/assets/b74658cf-4eff-4117-b187-270e321d8d34)


Administración de acceso:

![image](https://github.com/user-attachments/assets/19fe90db-241a-47da-a916-ae6c8e88b40c)


Bucket S3:

![image](https://github.com/user-attachments/assets/b65a11bb-f806-4c02-8003-db3a4c0f4e3e)


Covid Data (S3 Raw):

![image](https://github.com/user-attachments/assets/8f840bc6-0d82-4a3d-bafa-9b30430e5b14)


Covid Data (S3 Trusted):

![image](https://github.com/user-attachments/assets/15774704-8b44-4b42-bb63-a14857db3f2d)


Covid Data (S3 Refined):

![image](https://github.com/user-attachments/assets/681717b4-e438-4860-ad62-d404cfc8a642)


Consulta desde Athena:

![image](https://github.com/user-attachments/assets/af3e9025-2a9e-48b5-8540-4b860973727f)



# 5. otra información que considere relevante para esta actividad.

## Problemas encontrados:

El principal problema fue la creación del cluster, debido a que AWS mataba todos los clusters que intentaban crearse (posbiblemente debido a la alta demanda durante el fin de semana), arrojando un "Validation Error" tras 10 segundos de creación del cluster.

Solución inicial: Cambio de region de N. Virginia (us-east-1) a Oregon (us-west-2).

Sin embargo, Oregon presentó el mismo problema posteriormente.


Durante la creación de los steps y ejecución de código a manera de pruebas dentro de la aplicación de JupyterHub del cluster, se encontró con tiempos largos de espera para el procesamiento de operaciones que anteriormente no habían tomado tanto tiempo, lo que terminó llevando a la eliminación del cluster avanzado para la creación de uno nuevo.


Clusters creados debido al error de creación "Validation Error" (partiendo del clonado de un cluster que había funcionado perfectamente):

Oregon:
![image](https://github.com/user-attachments/assets/70adf00f-a083-4d6f-869a-9a46290bc357)

N. Virginia:

![image](https://github.com/user-attachments/assets/f8f27119-366d-4165-90d3-fca7bac618e9)

EDIT: El error resultó ser que AWS cancela la creación cuando se tiene algunos puertos abiertos en el security group donde se va a crear el cluster

