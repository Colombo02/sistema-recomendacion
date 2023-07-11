import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI


movies = pd.read_csv("dataset_clean/movies.csv") #Leemos el dataset

app = FastAPI()

@app.get("/peliculas_idioma/{idioma}")
def cantidad_peliculas_idioma(idioma: str):
    idioma = idioma.lower() #Paasamos el parametro a miniscula

    if idioma not in movies["original_language"].unique(): #Verificamos que el idioma ingresado este en el dataset
        return "ingrese un idioma disponible"
    else:
        cantidad_peliculas = len(movies[movies["original_language"] == idioma]) #Contamos las peliculas con ese idioma
        return {'idioma': idioma, 'cantidad': cantidad_peliculas}


@app.get("/peliculas_duracion/{pelicula}")
def peliculas_duracion(pelicula: str):
    pelicula = pelicula.lower() #Paasamos el parametro a miniscula

    if pelicula.lower() not in movies["title"].str.lower().values: #Verificamos que la pelicula ingresada este en el dataset
        return "Ingrese una película disponible"
    else:
        duracion = movies.loc[movies["title"].str.lower() == pelicula, 'runtime'].item() #Obtenemos la duracion de la pelicula
        anio = movies.loc[movies["title"].str.lower() == pelicula, 'release_year'].item() #Obtenemos el año de estreno
        return {'pelicula': pelicula.title(), 'duracion': duracion, 'anio': anio}

@app.get("/franquicia/{franquicia}")
def obtener_franquicia_detalle(franquicia: str):
    franquicia = franquicia.lower() #Paasamos el parametro a miniscula

    if franquicia.lower() not in movies["belongs_to_collection"].str.lower().values: #Verificamos que la franquicia ingresada este en el dataset
        return "ingrese una franquicia disponible"    
    else:
        franquicia_df = movies[movies["belongs_to_collection"].str.lower() == franquicia] #Filtramos todos las columnas/filas con esa franquicia
        cantidad_peliculas = len(franquicia_df) #Contamos la cantidad de peliculas
        ganancia_total = franquicia_df["revenue"].astype(float).sum() #Calculamos la ganancia total de la franquicia
        promedio = franquicia_df["revenue"].astype(float).mean() #Calculamos el primedio de la franquicia
        return {'franquicia': franquicia.title(), 'cantidad': cantidad_peliculas, 'ganancia_total': ganancia_total, 'ganancia_promedio': promedio}


@app.get("/peliculas_pais/{pais}")
def cantidad_peliculas_pais(pais: str):

    if pais.lower() not in movies["production_countries"].str.lower().values: #Verificamos que el pais ingresado este en el dataset
        return "Ingrese un pais disponible"
    
    cantidad_peliculas = len(movies[movies["production_countries"].str.lower() == pais.lower()]) #Contamos la cantidad de peliculas realizadas en ese pais.
    
    return {'pais':pais.title(), 'cantidad':cantidad_peliculas}

@app.get("/productoras_exitosas/{productora}")
def productoras_exitosas(productora: str):
    productora = productora.lower() #Paasamos el parametro a miniscula
    
    if productora.lower() not in movies["production_companies"].str.lower().values: #Verificamos que la productora ingresada este en el dataset
        return "ingrese una productora disponible"
    else:
        productora_df = movies[movies["production_companies"].str.lower() == productora] #Filtramos todos las columnas/filas con esa productora
        cantidad_peliculas = len(productora_df) #Contamos la cantidad de peliculas
        revenue_total = productora_df["revenue"].astype(float).sum() #Calculamos la ganancia total
        return {'productora':productora.title(), 'revenue_total':revenue_total, 'cantidad':cantidad_peliculas}


@app.get("/director/{director}")
def get_director(director: str):
    director = director.lower() #Paasamos el parametro a miniscula

    if director.lower() not in movies["director"].str.lower().values: #Verificamos que el director ingresado este en el dataset
        return "ingrese un director disponible"
    else:
        director_df = movies[movies["director"].str.lower() == director] #Filramos todos las columnas/filas con ese productor
        retorno_director = director_df["revenue"].astype(float).mean() #Calculamos el promedio de ganancias de las peliculas donde participo el director
        peliculas_director = director_df[["title", "release_date", "revenue", "budget", "return"]] #Filtramos esas columnas para obtener las peliculas con su estreno, ganancia, costo y ROI.
        
    peliculas = []
        
    for index, row in peliculas_director.iterrows(): #Iteramos cada fila añadiendolas a un diccionario segun su clave.
        pelicula = {
                'titulo': row['title'],
                'anio': row['release_date'],
                'retorno_pelicula': row['return'],
                'budget_pelicula': row['budget'],
                'revenue_pelicula': row['revenue']
                }
        peliculas.append(pelicula) #Añadimos el diccionario a la lista.
            
        respuesta = {
                'director': director.title(),
                'retorno_total_director': retorno_director,
                'peliculas': peliculas
                }
    return respuesta




data = pd.read_csv("dataset_clean/moviesML.csv") #Leemos el dataset
    
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['title'] + ' ' + data['genres'] + ' ' + data['vote_average'].astype(str)) #Calcular la matriz TF-IDF para la columna 'title'
    
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix) #Calculamos la matriz de similitud de coseno

@app.get("/recomendacion/{titulo}")
def recomendacion(titulo):
    titulo = titulo.lower() #Pasamos el parametro a miniscula.

    if titulo.lower() not in data['title'].str.lower().values: #Verificamos que el titulo este en el dataset
        return "ingrese una pelicula disponible"

    indices = pd.Series(data.index, index=data['title'].str.lower()).drop_duplicates() # Encontramos el índice de la película con el título dado
    idx = indices[titulo]

    sim_scores = list(enumerate(cosine_similarities[idx])) # Calculamos las puntuaciones de similitud de todas las películas con la película dada

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) # Ordenamos las películas por puntaje de similitud en orden descendente

    # Obtenemos los índices de las películas más similares (excluyendo la película dada)
    sim_scores = sim_scores[1:6]  # Obtenemos las 5 películas más similares
    movie_indices = [x[0] for x in sim_scores]

    respuesta_recomendacion = data['title'].iloc[movie_indices].tolist() # Devolvemos los títulos de las películas más similares en una lista
    return {'lista recomendada': respuesta_recomendacion}