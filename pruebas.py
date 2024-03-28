def conversion(x,y,eleccion):
    coor_x = len(str(x))
    coor_y = len(str(y))
    coor_finx = int()
    coor_finy = int()
    n = 0
    aux1 = coor_x #largo de coor x
    aux2 = coor_y #largo de coor y
    if eleccion == 1:
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
    if eleccion == "3":
        while n < coor_x:
            aux1 -= 1
            pos = (str(x)) [aux1]
            if pos == "A" or pos == "a":
                coor_finx = coor_finx + (10 * 16**n)
                n += 1
                continue

            if pos == "B" or pos == "b":
                coor_finx =  coor_finx + (11 * 16**n)
                n += 1
                continue

            if pos == "C" or pos == "c":
                coor_finx = coor_finx + (12 * 16**n)
                n += 1
                continue

            if pos == "D" or pos == "d":
                coor_finx = coor_finx + (13 * 16**n)
                n += 1
                continue

            if pos == "E" or pos == "e":
                coor_finx = coor_finx + (14 * 16**n)
                n += 1
                continue

            if pos == "F" or pos == "f":
                coor_finx = coor_finx + (15 * 16**n)
                n += 1
                continue
            if pos == "0":
                n += 1
                continue
            if pos == "1":
                coor_finx = coor_finx + (1 * 16**n)
                n += 1
                continue
            if pos == "2":
                coor_finx = coor_finx + (2 * 16**n)
                n += 1
                continue
            if pos == "3":
                coor_finx = coor_finx + (3 * 16**n)
                n += 1
                continue
            if pos == "4":
                coor_finx = coor_finx + (4 * 16**n)
                n += 1
                continue
            if pos == "5":
                coor_finx = coor_finx + (5 * 16**n)
                n += 1
                continue
            if pos == "6":
                coor_finx = coor_finx + (6 * 16**n)
                n += 1
                continue
            if pos == "7":
                coor_finx = coor_finx + (7 * 16**n)
                n += 1
                continue
            if pos == "8":
                coor_finx = coor_finx + (8 * 16**n)
                n += 1
                continue
            if pos == "9":
                coor_finx = coor_finx + (9 * 16**n)
                n += 1
                continue
        n=0
        while n < coor_y:
            aux1 -= 1
            pos = (str(y)) [aux1]
            if pos == "A" or pos == "a":
                coor_finy = coor_finy + (10 * 16**n)
                n += 1
                continue

            if pos == "B" or pos == "b":
                coor_finy =  coor_finy + (11 * 16**n)
                n += 1
                continue

            if pos == "C" or pos == "c":
                coor_finy = coor_finy + (12 * 16**n)
                n += 1
                continue

            if pos == "D" or pos == "d":
                coor_finy = coor_finy + (13 * 16**n)
                n += 1
                continue

            if pos == "E" or pos == "e":
                coor_finy = coor_finy + (14 * 16**n)
                n += 1
                continue

            if pos == "F" or pos == "f":
                coor_finy = coor_finy + (15 * 16**n)
                n += 1
                continue
            if pos == "0":
                n += 1
                continue
            if pos == "1":
                coor_finy = coor_finy + (1 * 16**n)
                n += 1
                continue
            if pos == "2":
                coor_finy = coor_finy + (2 * 16**n)
                n += 1
                continue
            if pos == "3":
                coor_finy = coor_finy + (3 * 16**n)
                n += 1
                continue
            if pos == "4":
                coor_finy = coor_finy + (4 * 16**n)
                n += 1
                continue
            if pos == "5":
                coor_finy = coor_finy + (5 * 16**n)
                n += 1
                continue
            if pos == "6":
                coor_finy = coor_finy + (6 * 16**n)
                n += 1
                continue
            if pos == "7":
                coor_finy = coor_finy + (7 * 16**n)
                n += 1
                continue
            if pos == "8":
                coor_finy = coor_finy + (8 * 16**n)
                n += 1
                continue
            if pos == "9":
                coor_finy = coor_finy + (9 * 16**n)
                n += 1
                continue
        return [coor_finx,coor_finy]



print("Elección")
z = input()
print("Eje X")
x = input()
print("Eje Y")
y = input()
print(conversion(x,y,z))