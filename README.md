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



# 5. otra información que considere relevante para esta actividad.



## Problemas encontrados:

El principal problema que se encontró durante el desarrollo de la actividad fue la configuración del Ingress para el acceso a la página, que finalmente se solucionó creando el ingress directamente por el dominio. Perdimos bastante tiempo intentando ingresar con la ip de algun nodo. también se tuvo problemas con la carga de archivos de configuración compartidos de Wordpress al NFS, resultando en dificultades para subir imágenes a la página desplegada.






