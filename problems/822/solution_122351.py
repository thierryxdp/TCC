def repetidos(lista):
    cont = 0
    i = 1
    while i<len(lista):
        if lista[i] == lista[i-1]:
             cont = cont +1
        i = i+1
    return cont