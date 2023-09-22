def repetidos(lista):
    """ a """
    contador=0
    lista2=lista[1:]
    for n in range(len(lista) -1):
        if lista[n]==lista2[n]:
            contador+=1
    return contador