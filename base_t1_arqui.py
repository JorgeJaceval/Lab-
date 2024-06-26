
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

def convertir(x,y,eleccion):
    #Esta función lleva a cabo los tres tipos de conversiones a decimal. Toma el input x e y, así como la elección del jugador (1,2 ó 3).

    coor_x = len(str(x))
    coor_y = len(str(y))
    coor_finx = int()
    coor_finy = int()
    pos = 0 #posición en el string
    aux1 = coor_x #largo de coor x
    aux2 = coor_y #largo de coor y

    if eleccion == "1":
        while pos < coor_x:
            aux1 -= 1
            num = (str(x))[aux1] #Empezamos a tomar el numero binario de izquierda a derecha
            #queremos verificar si es que num es un 0 o un 1
            if num == "1":
                coor_finx += 2**pos
                pos += 1
            if num == "0":
                pos += 1
                continue
        pos = 0
        while pos < coor_y:
            aux2 -= 1
            num = (str(y))[aux2] #Empezamos a tomar el numero binario de izquierda a derecha
            #queremos verificar si es que num es un 0 o un 1
            if num == "1":
                coor_finy += 2**pos
                pos += 1
            if num == "0":
                pos += 1
                continue
        return [coor_finx, coor_finy], 1
    
    if eleccion == "2":
        octal = "(" + x + "," + y + ")"
        total_left = 0
        total_right = 0
        oc_sample  = octal.split(",") #Lista con x e y en octal
        oc_left_samp = oc_sample[0] #Parte x en octal 
        oc_right_samp = oc_sample[1] #parte y en octal
        size_left_oc = len(oc_left_samp) - 1 #Tamaño del octal sin el parentesis
        size_right_oc = len(oc_right_samp) - 1 #Tamaño del octal sin el parentesis
        
        for character in oc_left_samp: #Recorre el input octal de x
            if character == "(" or character == ")":
                continue
            else:
                total_left += int(character) * (8**(size_left_oc - 1)) #Multiplica el número respectivo por 8 elevado a la posicion (contando desde 1) menos 1
                size_left_oc = size_left_oc - 1
        for character in oc_right_samp: #Recorre el input octal de y
            if character == "(" or character == ")":
                continue
            else: 
                total_right += int(character) * (8**(size_right_oc - 1)) #Multiplica el número respectivo por 8 elevado a la posicion (contando desde 1) menos 1
                size_right_oc = size_right_oc - 1
        return [total_left, total_right], 2 #Retorna x e y
    
    if eleccion == "3": #Mismo proceso que el binario, ya que la base sigue siendo el polinomio caracteristico.
        while pos < coor_x:
            aux1 -= 1
            num = (str(x)) [aux1]
            if num =="X" or num=="x":
                continue
            
            if num == "A" or num == "a":
                coor_finx = coor_finx + (10 * 16**pos)
                pos += 1
                continue

            if num == "B" or num == "b":
                coor_finx =  coor_finx + (11 * 16**pos)
                pos += 1
                continue

            if num == "C" or num == "c":
                coor_finx = coor_finx + (12 * 16**pos)
                pos += 1
                continue

            if num == "D" or num == "d":
                coor_finx = coor_finx + (13 * 16**pos)
                pos += 1
                continue

            if num == "E" or num == "e":
                coor_finx = coor_finx + (14 * 16**pos)
                pos += 1
                continue

            if num == "F" or num == "f":
                coor_finx = coor_finx + (15 * 16**pos)
                pos += 1
                continue
            if num == "0":
                pos += 1
                continue
            if num == "1":
                coor_finx = coor_finx + (1 * 16**pos)
                pos += 1
                continue
            if num == "2":
                coor_finx = coor_finx + (2 * 16**pos)
                pos += 1
                continue
            if num == "3":
                coor_finx = coor_finx + (3 * 16**pos)
                pos += 1
                continue
            if num == "4":
                coor_finx = coor_finx + (4 * 16**pos)
                pos += 1
                continue
            if num == "5":
                coor_finx = coor_finx + (5 * 16**pos)
                pos += 1
                continue
            if num == "6":
                coor_finx = coor_finx + (6 * 16**pos)
                pos += 1
                continue
            if num == "7":
                coor_finx = coor_finx + (7 * 16**pos)
                pos += 1
                continue
            if num == "8":
                coor_finx = coor_finx + (8 * 16**pos)
                pos += 1
                continue
            if num == "9":
                coor_finx = coor_finx + (9 * 16**pos)
                pos += 1
                continue
        pos=0
        while pos < coor_y:
            aux1 -= 1
            num = (str(y)) [aux1]
            if num =="X" or num=="x":
                continue
            if num == "A" or num == "a":
                coor_finy = coor_finy + (10 * 16**pos)
                pos += 1
                continue

            if num == "B" or num == "b":
                coor_finy =  coor_finy + (11 * 16**pos)
                pos += 1
                continue

            if num == "C" or num == "c":
                coor_finy = coor_finy + (12 * 16**pos)
                pos += 1
                continue

            if num == "D" or num == "d":
                coor_finy = coor_finy + (13 * 16**pos)
                pos += 1
                continue

            if num == "E" or num == "e":
                coor_finy = coor_finy + (14 * 16**pos)
                pos += 1
                continue

            if num == "F" or num == "f":
                coor_finy = coor_finy + (15 * 16**pos)
                pos += 1
                continue
            if num == "0":
                pos += 1
                continue
            if num == "1":
                coor_finy = coor_finy + (1 * 16**pos)
                pos += 1
                continue
            if num == "2":
                coor_finy = coor_finy + (2 * 16**pos)
                pos += 1
                continue
            if num == "3":
                coor_finy = coor_finy + (3 * 16**pos)
                pos += 1
                continue
            if num == "4":
                coor_finy = coor_finy + (4 * 16**pos)
                pos += 1
                continue
            if num == "5":
                coor_finy = coor_finy + (5 * 16**pos)
                pos += 1
                continue
            if num == "6":
                coor_finy = coor_finy + (6 * 16**pos)
                pos += 1
                continue
            if num == "7":
                coor_finy = coor_finy + (7 * 16**pos)
                pos += 1
                continue
            if num == "8":
                coor_finy = coor_finy + (8 * 16**pos)
                pos += 1
                continue
            if num == "9":
                coor_finy = coor_finy + (9 * 16**pos)
                pos += 1
                continue
        return [coor_finx,coor_finy], 3

def hay_nave (lista_enemigos, x, y):
    #Esta función procesa la opción elegida por el usuario para hacerla coincidir con la base de la nave en tales coordenadas, si es que coincide, la nave se borra
    #de la lista de enemigos y se reemplaza por un "?" 
    for c in lista_enemigos:
        if c[0] == int(x):
            if c[1] == int(y):
                #Ambas coordenadas coinciden, hay nave
                return True
    else:
        print("¡Vaya! No le has dado a ninguna nave")
        return False
            
juego,enemigos = crear_mapa(5,2)
t = 1 # Contador de turnos
end  = False # Indicador del estado del juego.
while end != True:
    visualizar_mapa(juego)
    print("Turno " + str(t))
    elec = input("Ingrese su elección \n 1. Binaria \n 2. Octal \n 3. Hexadecimal\n")
    x = input ("Ingrese coordenada X: ")
    y = input("Ingrese coordenada Y: ")
    pos_decimal, elec = convertir(x, y, elec)
    if hay_nave(enemigos, pos_decimal[0], pos_decimal[1]):
        #Primero debo conseguir el tipo ("letra") de la nave en cuestion
        tipo_nave = juego[pos_decimal[0]][pos_decimal[1]] #Esta es la letra de la nave
        if tipo_nave == "X":
            tipo_nave = 1
        elif tipo_nave == "Y":
            tipo_nave = 2
        elif tipo_nave == "Z":
            tipo_nave = 3
        if tipo_nave == elec: #Verifica si la nave corresponde al tipo elegido
            enemigos.remove((pos_decimal[0], pos_decimal[1])) #Quita al enemigo hundido de la lista de enemigos
            juego[pos_decimal[0]][pos_decimal[1]] = "?" #Remueve la nave del mapa y lo reemplaza por "?"
            print("¡Le has dado rico!")
            if not enemigos: #verifica que la lista esté vacia para terminar el juego
                end = True
        else:
            print("No le sabes a elegir bases")
    t += 1
print("\nHas matado a todos\n")
print("Felicidades, has perdido tu tiempo con este juego!")
