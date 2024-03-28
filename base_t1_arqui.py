
import random
from prettytable import PrettyTable

def crear_mapa(size,cantidad_naves):
    listaposnaves = []
    lista = []
    for i in range(0,size*2):
        row = []
        for j in range(0,size):
            row.append('?')
        lista.append(row)

    for i in range(0,cantidad_naves):
        cordx = random.randint(0,2*size-1)
        cordy = random.randint(0,size-1)
        tipo = random.randint(0,2)
        tipos = 'XYZ'
        if lista[cordx][cordy] != '?':
            print("Coordenadas de nave", i, "colisionaron con otra nave, no se añade al mapa")
            continue
        else:
            lista[cordx][cordy] = tipos[tipo]
            listaposnaves.append((cordx,cordy))


    return(lista,listaposnaves)

def visualizar_mapa(lista):
    
    tabla = PrettyTable()

    
    tabla.field_names = [''] + list(range(len(lista[0])))

    
    for numberfila, row in enumerate(lista):
        row_data = [numberfila] + row
        tabla.add_row(row_data)

    
    print(tabla)


juego,enemigos = crear_mapa(10,10)
visualizar_mapa(juego)

a = input()
x = input()
y= input()

def binario():
    coor_x = len(str(x))
    coor_y = len(str(y))
    coor_finx = str()
    coor_finy = str()
    n = 0
    aux1 = coor_x
    aux2 = coor_y
    while n < coor_x:
        pos = (str(x))[aux1-1] #Empezamos a tomar el numero binario de izquierda a derecha
        #queremos verificar si es que pos es un 0 o un 1
        if pos == 1:
            coor_finx += 2**n
        if pos == 0:
            continue
        n += 1





if a == 1:
    input()

