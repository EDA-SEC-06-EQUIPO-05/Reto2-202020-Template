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

def loadData(catalog, moviesfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadMovs(catalog, moviesfile)
    #loadTags(catalog, tagsfile)
    #loadBooksTags(catalog, booktagsfile)


def loadMovs(catalog, moviesfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    dialect = csv.excel()
    dialect.delimiter=";"
    moviesfile = cf.data_dir + moviesfile
    input_file = csv.DictReader(open(moviesfile),dialect=dialect)
    for movie in input_file:
        model.addMovie(catalog, movie)
        directors = movie['original_language'].split(",")  # Se obtienen los lenguajes
'''
def loadTags(catalog, tagsfile):
    """
    Carga en el catalogo los tags a partir de la informacion
    del archivo de etiquetas
    """
    tagsfile = cf.data_dir + tagsfile
    input_file = csv.DictReader(open(tagsfile))
    for tag in input_file:
        model.addTag(catalog, tag)


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

def booksSize(catalog):
    """Numero de libros leido
    """
    return model.booksSize(catalog)


def authorsSize(catalog):
    """Numero de autores leido
    """
    return model.authorsSize(catalog)


def tagsSize(catalog):
    """Numero de tags leido
    """
    return model.tagsSize(catalog)


def getBooksByAuthor(catalog, authorname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getBooksByAuthor(catalog, authorname)
    return authorinfo


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

