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

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

moviesfile = 'DetailsSmall.csv'
#tagsfile = 'GoodReads/tags.csv'
#booktagsfile = 'GoodReads/book_tags-small.csv'


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________


def printAuthorData(author):
    """
    Imprime los libros de un autor determinado
    """
    if author:
        print('Autor encontrado: ' + author['name'])
        print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(lt.size(author['books'])))
        iterator = it.newIterator(author['books'])
        while it.hasNext(iterator):
            book = it.next(iterator)
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
    else:
        print('No se encontro el autor')


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
    print("1- Cargar datos")
    print("2- Inicializar Catálogo")
    print("3- Cargar información en el catálogo")
    print("4- Consultar los libros de un año")
    print("5- Consultar los libros de un autor")
    print("6- Consultar los Libros por etiqueta")
    print("0- Salir")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs) == 1:
        archivo= input("Ingrese el nombre del archivo que desea cargar: ")
        print("Cargando lista de datos... ")
        lista_datos= controller.cargar_datos(archivo)
        primer_elemento= controller.datos_primer_elemento(lista_datos)
        ultimo_elemento= controller.datos_ultimo_elemento(lista_datos)
        print("Se cargo el registro de "+str(lt.size(lista_datos))+" peliculas. A continuación esta la informacion de la primera y ultima pelicula del registro: \n")
        print("Nombre de la pelicula: "+primer_elemento[0]+", Fecha de estreno: "+primer_elemento[1]+", Calificacion promedio: "+primer_elemento[2]+", Cantidad de votos: "+primer_elemento[3]+", Idioma original: "+primer_elemento[4]+"\n")
        print("Nombre de la pelicula: "+ultimo_elemento[0]+", Fecha de estreno: "+ultimo_elemento[1]+", Calificacion promedio: "+ultimo_elemento[2]+", Cantidad de votos: "+ultimo_elemento[3]+", Idioma original: "+ultimo_elemento[4]+"\n")

    elif int(inputs) == 2:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()

    elif int(inputs) == 3:
        print("Cargando información de los archivos ....")
        controller.loadData(cont, moviesfile)
        print('Películas cargadas cargados: ' + str(controller.moviesSize(cont)))
        print('Autores cargados: ' + str(controller.authorsSize(cont)))
        print('Géneros cargados: ' + str(controller.tagsSize(cont)))

    elif int(inputs) == 4:
        number = input("Buscando libros del año?: ")
        books = controller.getBooksYear(cont, int(number))
        printBooksbyYear(books)

    elif int(inputs) == 5:
        authorname = input("Nombre del autor a buscar: ")
        authorinfo = controller.getBooksByAuthor(cont, authorname)
        printAuthorData(authorinfo)

    elif int(inputs) == 6:
        label = input("Etiqueta a buscar: ")
        books = controller.getBooksByTag(cont, label)
        printBooksbyTag(books)
    else:
        sys.exit(0)
sys.exit(0)

