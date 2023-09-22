def filtra_pares(tupla1):
    elem1_2 = int(elem1[0])
    elem2_2 = int(elem2[1])
    elem3_2 = int(elem3[2])
    elem4_2 = int(elem4[3])
    tupla = ()
    if elem1_2 % 2 == 0:
        tupla += ((tupla1[0]),)
    if elem2_2 % 2 == 0:
        tupla += ((tupla1[1]),)
    if elem2_2 % 2 == 0:
        tupla += ((tupla1[2]),)
    if elem4_2 % 2 == 0:
        tupla += ((tupla1[3]),)
    return tupla