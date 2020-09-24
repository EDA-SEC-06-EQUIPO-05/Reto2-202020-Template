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
               'producers': None,
               'directors': None,
               'vote_count': None,
               'release_date': None}

    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)

    catalog['producers'] = mp.newMap(200,109345121,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareProducersByName)
    catalog['directors'] = mp.newMap(200,109345121,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareDirectorsByName)
    catalog['movieIds'] = mp.newMap(200,109345121,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMovieIds)
    catalog['genres'] = mp.newMap(200,109345121,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMoviesbyGenre)
    catalog['countries'] = mp.newMap(200,109345121,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMoviesbyCountry)

    
    return catalog


def newProducer(name):
    """
    Crea una nueva estructura para modelar las peliculas de una productora
    y su promedio de ratings
    """
    producer = {'name': "", "movies": None,  "average_rating": 0}
    producer['name'] = name
    producer['movies'] = lt.newList('SINGLE_LINKED', compareProducersByName)
    return producer

def newDirector(name):
    """
    Crea una nueva estructura para modelar las peliculas de un director
    y su promedio de ratings
    """
    director = {'name': "", "movies": None,  "average_rating": 0}
    director['name'] = name
    director['movies'] = lt.newList('SINGLE_LINKED', compareDirectorsByName)
    return director

def newGenre(name):
    """
    Crea una nueva estructura para modelar los generos, las peliculas correspondientes del catalogo
    y su promedio de ratings
    """
    genre = {'name': "", "movies": None,  "average_vote_count": 0, "size":0}
    genre['name'] = name
    genre['movies'] = lt.newList('SINGLE_LINKED', compareMoviesbyGenre)
    return genre

def newCountry(name):
    """
    Crea una nueva estructura para modelar los generos, las peliculas correspondientes del catalogo
    y su promedio de ratings
    """
    country = {'name': "", "movies": None,  "average_vote_count": 0, "size":0}
    country['name'] = name
    country['movies'] = lt.newList('SINGLE_LINKED', compareMoviesbyCountry)
    return country

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
    Esta funcion adiciona una pelicula a la lista de peliculas,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    #print(movie)
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['movieIds'], movie['id'], movie)
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
'''

def addMovieProducer(catalog, producername, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    #print(movie)
    producers = catalog['producers']
    existproducer = mp.contains(producers, producername)
    if existproducer:
        entry = mp.get(producers, producername)
        producer = me.getValue(entry)
    else:
        producer = newProducer(producername)
        mp.put(producers, producername, producer)
    lt.addLast(producer['movies'], movie)
    #producer['id'] = movie['id']

    produceravg = producer['average_rating']
    movieavg = movie['vote_average']
    if (produceravg == 0.0):
        producer['average_rating'] = float(movieavg)
    else:
        producer['average_rating'] = round((produceravg + float(movieavg)) / 2,2)

def addMovieDirector(catalog, directorname, details):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    #print(movie)
    directors = catalog['directors']
    existdirector = mp.contains(directors, directorname)
    if existdirector:
        entry = mp.get(directors, directorname)
        director = me.getValue(entry)
    else:
        director = newDirector(directorname)
        mp.put(directors, directorname, director)

    #print(casting['director_name'])

    #lt.addLast(director['movies'], casting)
    lt.addLast(director['movies'], details)
    #print(director['movies'])

    directoravg = director['average_rating']
    movieavg = details['vote_average']
    if (directoravg == 0.0):
        director['average_rating'] = float(movieavg)
    else:
        director['average_rating'] = round((directoravg + float(movieavg)) / 2,2)

def AddMovieByGenre(catalog, genrename, details):

    genres = catalog['genres']
    existgenre = mp.contains(genres, genrename)
    if existgenre:
        entry = mp.get(genres, genrename)
        genre = me.getValue(entry)
    else:
        genre = newDirector(genrename)
        mp.put(genres, genrename, genre)

    #print(casting['director_name'])

    #lt.addLast(director['movies'], casting)
    lt.addLast(genre['movies'], details)
    #print(director['movies'])

    genreavg = genre['average_rating']
    movieavg = details['vote_average']
    if (genreavg == 0.0):
        genre['average_rating'] = float(movieavg)
    else:
        genre['average_rating'] = round((genreavg + float(movieavg)) / 2,2)

def AddMovieByCountry(catalog, countryname, details, casting):

    countries = catalog['countries']
    existcountry = mp.contains(countries, countryname)
    if existcountry:
        entry = mp.get(countries, countryname)
        country = me.getValue(entry)
    else:
        country = newCountry(countryname)
        mp.put(countries, countryname, country)

    #print(casting['director_name'])

    #lt.addLast(country['movies'], casting)
    lt.addLast(country['movies'], details)
    #print(director['movies'])

    countryavg = country['average_rating']
    movieavg = details['vote_average']
    if (countryavg == 0.0):
        country['average_rating'] = float(movieavg)
    else:
        country['average_rating'] = round((countryavg + float(movieavg)) / 2,2)


'''    
    genero_arr= genero.split("|") 
    for tipo in genero_arr:
        genres = catalog['genres']
        existgenre = mp.contains(genres, tipo)
        if existgenre:
            entry = mp.get(genres, tipo)
            genre = me.getValue(entry)
        else:
            genre = newGenre(tipo)
            mp.put(genres, tipo, genre)
        lt.addLast(genre['movies'], movie)


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


def getMoviesbyProducer(catalog, producername):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    producer = mp.get(catalog['producers'], producername)
    lista_peliculas = None
    if producer:
        lista_peliculas = me.getValue(producer)
    return lista_peliculas

def getMoviesbyDirector(catalog, directorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    director = mp.get(catalog['directors'], directorname)
    lista_peliculas = None
    if director:
        lista_peliculas = me.getValue(director)
    return lista_peliculas


def getMoviesbyGenre(catalog, genrename):
    """
    Retornar la lista de libros asociados a un tag
    """
    genre = mp.get(catalog['genres'], genrename)
    lista_peliculas = None
    if genre:
        lista_peliculas = me.getValue(genre)
    return lista_peliculas

def getMoviesbyCountry(catalog, countryname):
    """
    Retornar la lista de libros asociados a un tag
    """
    country = mp.get(catalog['countries'], countryname)
    lista_peliculas = None
    if country:
        lista_peliculas = me.getValue(country)
    return lista_peliculas


def moviesSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['movies'])


def producersSize(catalog):
    """
    Numero de autores en el catalogo
    """
    return mp.size(catalog['producers'])


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


def compareMapMovieIds(id, entry):
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


def compareProducersByName(keyname, producer):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    produentry = me.getKey(producer)
    if (keyname == produentry):
        return 0
    elif (keyname > produentry):
        return 1
    else:
        return -1

def compareDirectorsByName(keyname, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    directentry = me.getKey(director)
    if (keyname == directentry):
        return 0
    elif (keyname > directentry):
        return 1
    else:
        return -1

def compareMoviesbyGenre(keyname, genre):
    """
    Compara dos generos. El primero es una cadena
    y el segundo un entry de un map
    """
    genero = me.getKey(genre)
    if (keyname == genero):
        return 0
    elif (keyname > genero):
        return 1
    else:
        return -1

def compareMoviesbyCountry(keyname, country):
    """
    Compara dos generos. El primero es una cadena
    y el segundo un entry de un map
    """
    pais = me.getKey(country)
    if (keyname == pais):
        return 0
    elif (keyname > pais):
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
    lt_datos.append(datos["original title"])
    '''
    lt_datos.append(datos["release_date"])
    lt_datos.append(datos["vote_average"])
    lt_datos.append(datos["vote_count"])
    lt_datos.append(datos["spoken_languages"])
'''
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

"""def moviesbygenre(genero,catalog,lista_pelis):

    cantidad_peliculas_genero= 0
    lista_peliculas= []
    suma_votos= 0
    cuenta= 0
    promedio_votos= 0
    gender= mp.get(catalog["genre"], genero)
    if gender:
        lista_peliculas = me.getValue(gender)
        cantidad_peliculas_genero= len(lista_peliculas)
    for pelis in lista_pelis:
        if pelis["original_title"]==lista_peliculas[cuenta]:
            suma_votos+= float(pelis["vote_count"])
            cuenta+= 1

    promedio_votos= suma_votos/cantidad_peliculas_genero

    return (cantidad_peliculas_genero,promedio_votos,lista_peliculas)
    """


