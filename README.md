# Proyecto Individual : Sistema de Recomendación</center>
![Logo](https://github.com/Colombo02/sistema-recomendacion/blob/main/src/hernry.png)

# <center>Machine Learning Operations (MLOps)</center> 
![Logo](https://github.com/Colombo02/sistema-recomendacion/blob/main/src/MlOps.png)

## Rol a desarrollar:
El obejtivo es crear un modelo de ML que soluciona un problema de negocio: un sistema de recomendación de películas.
Al ver los datos se observa que no estan limpios y hay que hacer un trabajo de Data Engineer para limpiarlos y asi poder crear el modelo de ML. Se debe hacer un trabajo rapido y tener un MVP (Minimum Viable Product) para el cierre del proyecto.

## ETL
Nos indican que solamente debemos realizar el **ETL (extract, transform, load)** en algunos campos. 

* Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, hay que desanidarlos

* Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.

* Los valores nulos del campo release date deben eliminarse.

* De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.

* Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

* Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,poster_path y homepage.

## Desarrollo API

Se crean 6 funciones para los endpoints que se consumirán en la API con el decorador (@app.get(‘/’)).

* **def peliculas_idioma( Idioma: str ):** Se ingresa un idioma (silabas del idioma en ingles). Devuelve la cantidad de películas producidas en ese idioma.

* **def peliculas_duracion( Pelicula: str ):** Se ingresa una pelicula. Devuelve la duracion y el año.

* **def franquicia( Franquicia: str ):** Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio

* **def peliculas_pais( Pais: str ):** Se ingresa un país (como están escritos en el dataset), retornando la cantidad de peliculas producidas en el mismo.

* **def productoras_exitosas( Productora: str ):** Se ingresa la productora, retornando el revunue total y la cantidad de peliculas que realizo.

* **def get_director( nombre_director ):** Se ingresa el nombre de un director que se encuentre dentro de un dataset, devolviendo el retorno promedio por pelicula. Además de devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

## EDA

Se realiza un **EDA (Exploratory Data Analysis)** para observar las relaciones, distrbuciones, outliers, etc.

## Sistema de Recomendación

Recomienda películas a los usuarios basándose en películas similares, se ordenan según el score de similaridad y devuelve una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Para el modelo se utilizo la **similitud del coseno**.

[Sistema de recomendacion](https://sistema-recomendacion-f2hj.onrender.com/docs)

## Deployment

Se utilizo **Render.com** para hacer el deploy de la API.

## Diccionario de Datos

[Diccionario](https://github.com/Colombo02/sistema-recomendacion/blob/main/Diccionario%20de%20Datos.pdf)

## Dataset

[Datasets](https://drive.google.com/drive/folders/1mfUVyP3jS-UMdKHERknkQ4gaCRCO2e1v)

[Dataset_limpio](https://github.com/Colombo02/sistema-recomendacion/tree/main/dataset_clean)

## Linkedin

[Linkedin](https://linkedin.com/in/tomascolombo/)

## Video Youtube

[Youtube](https://youtube.com/video/Lj89lTLlr2g)
