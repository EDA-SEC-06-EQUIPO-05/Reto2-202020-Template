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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config
from time import process_time 

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

#moviesfile = 'Details.csv'
#tagsfile = 'GoodReads/tags.csv'
#booktagsfile = 'GoodReads/book_tags-small.csv'


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________


def printProducerData(producer):
    """
    Imprime los libros de un autor determinado
    """
    if producer:
        print('Productora encontrada: ' + producer['name'])
        print('Promedio: ' + str(producer['average_rating']))
        print('Total de peliculas: ' + str(lt.size(producer['movies'])))
        iterator = it.newIterator(producer['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['title'])
    else:
        print('No se encontro a la productora')

def printDirectorData(director):
    """
    Imprime los libros de un autor determinado
    """
    if director:
        print('Director encontrado: ' + director['name'])
        print('Promedio: ' + str(director['average_rating']))
        print('Total de peliculas: ' + str(lt.size(director['movies'])))
        iterator = it.newIterator(director['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['id'])
            #print(movie)
    else:
        print('No se encontro al director')


def printBooksbyTag(books):
    """
    Imprime los libros que han sido clasificados con
    una etiqueta
    """
    print('Se encontraron: ' + str(lt.size(books)) + ' Libros')
    iterator = it.newIterator(books)
    while it.hasNext(iterator):
        book = it.next(iterator)
        print(book['title'])


def printBooksbyYear(books):
    """
    Imprime los libros que han sido publicados en un
    año
    """
    print('Se encontraron: ' + str(lt.size(books)) + ' Libros')
    iterator = it.newIterator(books)
    while it.hasNext(iterator):
        book = it.next(iterator)
        print(book['title'])
    
# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar datos")
    print("3- Consultar las películas de una productora")
    print("4- Consultar las películas de un director")
    print("0- Salir")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()
        #print(cont)

    elif int(inputs) == 2:
        details = input("Ingrese el nombre del archivo de detalles que desea cargar: ")
        casting = input("Ingrese el nombre del archivo de elenco que desea cargar: ")
        print("Cargando lista de datos... ")
        #t1_start = process_time() #tiempo inicial
        #lista_datos= controller.cargar_datos(archivo)
        controller.loadData(cont, details, casting)
        print('Películas cargadas cargados: ' + str(controller.moviesSize(cont)))
        #t1_stop = process_time() #tiempo final
        #print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
        #print(lista_datos)
        #primer_elemento= controller.datos_primer_elemento(lista_datos)
        #ultimo_elemento= controller.datos_ultimo_elemento(lista_datos)
        #print("Se cargo el registro de "+str(lt.size(lista_datos))+" peliculas. A continuación esta la informacion de la primera y ultima pelicula del registro: \n")
        #print("Nombre de la pelicula: "+primer_elemento[0]+", Fecha de estreno: "+primer_elemento[1]+", Calificacion promedio: "+primer_elemento[2]+", Cantidad de votos: "+primer_elemento[3]+", Idioma original: "+primer_elemento[4]+"\n")
        #print("Nombre de la pelicula: "+ultimo_elemento[0]+", Fecha de estreno: "+ultimo_elemento[1]+", Calificacion promedio: "+ultimo_elemento[2]+", Cantidad de votos: "+ultimo_elemento[3]+", Idioma original: "+ultimo_elemento[4]+"\n")

    elif int(inputs) == 3:
        producername = input("Nombre de la productora a buscar: ")
        #t1_start = process_time() #tiempo inicial
        producerinfo = controller.getMoviesbyProducer(cont, producername)
        printProducerData(producerinfo)
        #t1_stop = process_time() #tiempo final
        #print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

    elif int(inputs) == 4:
        directorname = input("Nombre del director a buscar: ")
        directorinfo = controller.getMoviesbyDirector(cont, directorname)
        printDirectorData(directorinfo)
    else:
        sys.exit(0)
sys.exit(0)

