"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(catalog, detailsfile, castingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    dialect = csv.excel()
    dialect.delimiter=";"
    detailsfile = cf.data_dir + detailsfile
    input_file = csv.DictReader(open(detailsfile, encoding='utf-8'),dialect=dialect)
    #open(config.data_dir + archivo, encoding="utf-8") as csvfile:
    for details in input_file:
        model.addMovie(catalog, details)
        producers = details['production_companies'].split(",")  # Se obtienen las productoras
        for producer in producers:
            model.addMovieProducer(catalog, producer.strip(), details)
        genres_peli= details["genres"].split(",")
        for genre in genres_peli:
            model.AddMovieByGenre(catalog,genre.strip(),details)
    castingfile = cf.data_dir + castingfile
    input_c_file = csv.DictReader(open(castingfile, encoding='utf-8'),dialect=dialect)
    #open(config.data_dir + archivo, encoding="utf-8") as csvfile:
    for casting in input_c_file:
        directors = casting['director_name'].split(",")  # Se obtienen los directores
        for director in directors:
            model.addMovieDirector(catalog, director.strip(), details, casting)



    #loadDetails(catalog, detailsfile)
    #loadCasting(catalog, castingfile)
    #loadBooksTags(catalog, booktagsfile)

'''
def loadDetails(catalog, detailsfile):
    """
    Carga cada una de las lineas del archivo details.
    - Se agrega cada productora al catalogo de peliculas
    - Por cada pelicula se encuentran sus productoras y por cada
      productora, se crea una lista con sus peliculas
    """
    dialect = csv.excel()
    dialect.delimiter=";"
    detailsfile = cf.data_dir + detailsfile
    input_file = csv.DictReader(open(detailsfile, encoding='utf-8'),dialect=dialect)
    #open(config.data_dir + archivo, encoding="utf-8") as csvfile:
    for details in input_file:
        model.addMovie(catalog, details)
        producers = details['production_companies'].split(",")  # Se obtienen las productoras
        for producer in producers:
            model.addMovieProducer(catalog, producer.strip(), details)

def loadCasting(catalog, castingfile):
    """
    Carga cada una de las lineas del archivo casting.
    - Se agrega cada director al catalogo de peliculas
    - Por cada pelicula se encuentran sus directores y por cada
      director, se crea una lista con sus peliculas
    """
    dialect = csv.excel()
    dialect.delimiter=";"
    castingfile = cf.data_dir + castingfile
    input_file = csv.DictReader(open(castingfile, encoding='utf-8'),dialect=dialect)
    #open(config.data_dir + archivo, encoding="utf-8") as csvfile:
    for casting in input_file:
        directors = casting['director_name'].split(",")  # Se obtienen los directores
        for director in directors:
            model.addMovieDirector(catalog, director.strip(), casting)
'''
'''
def loadCasting(catalog, castingfile):
    """
    Carga en el catalogo los tags a partir de la informacion
    del archivo de etiquetas
    """
    castingfile = cf.data_dir + castingfile
    input_file = csv.DictReader(open(castingfile))
    for cast in input_file:
        model.addCast(catalog, cast)

def loadBooksTags(catalog, booktagsfile):
    """
    Carga la información que asocia tags con libros.
    Primero se localiza el tag y se le agrega la información leida.
    Adicionalmente se le agrega una referencia al libro procesado.
    """
    booktagsfile = cf.data_dir + booktagsfile
    input_file = csv.DictReader(open(booktagsfile))
    for tag in input_file:
        model.addBookTag(catalog, tag)

'''
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def moviesSize(catalog):
    """Numero de libros leido
    """
    return model.moviesSize(catalog)


def producersSize(catalog):
    """Numero de autores leido
    """
    return model.producersSize(catalog)


def tagsSize(catalog):
    """Numero de tags leido
    """
    return model.tagsSize(catalog)


def getMoviesbyProducer(catalog, producername):
    """
    Retorna los libros de un autor
    """
    producerinfo = model.getMoviesbyProducer(catalog, producername)
    return producerinfo

def getMoviesbyDirector(catalog, directorname):
    """
    Retorna los libros de un autor
    """
    directorinfo = model.getMoviesbyDirector(catalog, directorname)
    return directorinfo


def getBooksByTag(catalog, tagname):
    """
    Retorna los libros que han sido marcados con
    una etiqueta
    """
    books = model.getBooksByTag(catalog, tagname)
    return books


def getBooksYear(catalog, year):
    """
    Retorna los libros que fueron publicados
    en un año
    """
    books = model.getBooksByYear(catalog, year)
    return books

def datos_primer_elemento(lista):
    primer_ele= model.element_data(lista,"primera")
    return primer_ele

def datos_ultimo_elemento(lista):
    ultimo_ele= model.element_data(lista,"ultima")
    return ultimo_ele

def cargar_datos(archivo):

    lista_data= model.load_file(archivo)
    return lista_data

def pelis_genero(catalog,genero,lista_pelis):

    tupla_genero= model.moviesbygenre(genero,catalog,lista_pelis)
    return tupla_genero

