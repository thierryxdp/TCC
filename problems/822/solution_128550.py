def repetidos(lista_num):
    i = 0
    repetiu = 0
    while i < len(lista_num) -1:
        if lista_num[i] == lista_num[i+1]:
            repetiu += 1
        i += 1
    return repetiu