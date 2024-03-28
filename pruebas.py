def binario(x,y):
    coor_x = len(str(x))
    coor_y = len(str(y))
    coor_finx = int()
    coor_finy = int()
    n = 0
    aux1 = coor_x #largo de coor x
    aux2 = coor_y #largo de coor y

    while n < coor_x:
        aux1 -= 1
        pos = (str(x))[aux1] #Empezamos a tomar el numero binario de izquierda a derecha
        #queremos verificar si es que pos es un 0 o un 1
        if pos == "1":
            coor_finx += 2**n
            n += 1
        if pos == "0":
            n += 1
            continue
    n = 0
    while n < coor_y:
        aux2 -= 1
        pos = (str(y))[aux2] #Empezamos a tomar el numero binario de izquierda a derecha
        #queremos verificar si es que pos es un 0 o un 1
        if pos == "1":
            coor_finy += 2**n
            n += 1
        if pos == "0":
            n += 1
            continue
    return [coor_finx, coor_finy]


print("Eje X")
x=input()
print("Eje Y")
y=input()
print(binario(x,y))
