def repetidos(lista):
    contador=-1
    aux=0
    for n in lista:
        contador += 1
        if n == lista[contador]:
            aux +=1
    return aux