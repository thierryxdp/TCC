def repetidos(lista):
    """ """
    atual = []
    proximo = []
    cont = 1
    
    for i in lista:
        proximo = lista[cont]
        if proximo == i:
            cont += 1
    return cont