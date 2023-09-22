def faltante(lista):
    """ """
    lista.sort()
    atual = []
    proximo = []
    cont = 1
    for i in lista:
        proximo = lista[cont]
        if proximo == i+1:
            cont += 1
        else:
        	cont = i
            break
    return cont