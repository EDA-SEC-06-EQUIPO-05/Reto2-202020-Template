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
import config
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'movies': None,
               'title': None,
               'original_language': None,
               'vote_average': None,
               'vote_count': None,
               'release_date': None}

    catalog['movies'] = lt.newList('SINGLE_LINKED', comparemoviesIds)
    catalog['title'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapmoviesIds)
    catalog['original_language'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareLanguage)
    catalog['vote_average'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareAverage)
    catalog['vote_count'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareCount)
    catalog['release_date'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareMapRelease)

    return catalog


def newMovie(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    author = {'name': "", "books": None,  "average_rating": 0}
    author['name'] = name
    author['books'] = lt.newList('SINGLE_LINKED', compareAuthorsByName)
    return author


def newTagBook(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name': '',
           'tag_id': '',
           'total_books': 0,
           'books': None,
           'count': 0.0}
    tag['name'] = name
    tag['tag_id'] = id
    tag['books'] = lt.newList()
    return tag


# Funciones para agregar informacion al catalogo


def addMovie(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['movieIds'], movie['details_movies_id'], movie)
    #addBookYear(catalog, book)

'''
def addBookYear(catalog, book):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    years = catalog['years']
    pubyear = book['original_publication_year']
    pubyear = int(float(pubyear))
    existyear = mp.contains(years, pubyear)
    if existyear:
        entry = mp.get(years, pubyear)
        year = me.getValue(entry)
    else:
        year = newYear(pubyear)
        mp.put(years, pubyear, year)
    lt.addLast(year['books'], book)


def newYear(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "books": None}
    entry['year'] = pubyear
    entry['books'] = lt.newList('SINGLE_LINKED', compareReleased)
    return entry


def addMovieDirector(catalog, directorname, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    directors = catalog['director']
    existdirector = mp.contains(directors, directorname)
    if existdirector:
        entry = mp.get(directors, directorname)
        director = me.getValue(entry)
    else:
        director = newAuthor(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['books'], book)

    authavg = author['average_rating']
    bookavg = book['average_rating']
    if (authavg == 0.0):
        author['average_rating'] = float(bookavg)
    else:
        author['average_rating'] = (authavg + float(bookavg)) / 2

def addTag(catalog, tag):
    """
    Adiciona un tag a la tabla de tags dentro del catalogo
    """
    newtag = newTagBook(tag['tag_name'], tag['tag_id'])
    mp.put(catalog['tags'], tag['tag_name'], newtag)
    mp.put(catalog['tagIds'], tag['tag_id'], newtag)


def addBookTag(catalog, tag):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    bookid = tag['goodreads_book_id']
    tagid = tag['tag_id']
    entry = mp.get(catalog['tagIds'], tagid)

    if entry:
        tagbook = mp.get(catalog['tags'], me.getValue(entry)['name'])
        tagbook['value']['total_books'] += 1
        tagbook['value']['count'] += int(tag['count'])
        book = mp.get(catalog['bookIds'], bookid)
        if book:
            lt.addLast(tagbook['value']['books'], book['value'])
'''

# ==============================
# Funciones de consulta
# ==============================


def getBooksByAuthor(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    author = mp.get(catalog['authors'], authorname)
    if author:
        return me.getValue(author)
    return None


def getBooksByTag(catalog, tagname):
    """
    Retornar la lista de libros asociados a un tag
    """
    tag = mp.get(catalog['tags'], tagname)
    books = None
    if tag:
        books = me.getValue(tag)['books']
    return books


def booksSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['movies'])


def authorsSize(catalog):
    """
    Numero de autores en el catalogo
    """
    return mp.size(catalog['authors'])


def tagsSize(catalog):
    """
    Numero de tags en el catalogo
    """
    return mp.size(catalog['tags'])


def getBooksByYear(catalog, year):
    """
    Retorna los libros publicados en un año
    """
    year = mp.get(catalog['years'], year)
    if year:
        return me.getValue(year)['books']
    return None


# ==============================
# Funciones de Comparacion
# ==============================


def compareMoviesIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1


def compareLanguage(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def compareAverage(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1


def compareCount(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0


def compareMapRelease(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0


def compareRelease(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0
    
def element_data(lista,orden):

    lt_datos= []
    if orden== "primera":
        datos= lt.firstElement(lista)
    elif orden== "ultima":
        datos= lt.lastElement(lista)
    lt_datos.append(datos["original_title"])
    lt_datos.append(datos["release_date"])
    lt_datos.append(datos["vote_average"])
    lt_datos.append(datos["vote_count"])
    lt_datos.append(datos["spoken_languages"])

    return lt_datos

def load_file (archivo):
    lst=lt.newList("ARRAY_LIST")
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(config.data_dir + archivo, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst
