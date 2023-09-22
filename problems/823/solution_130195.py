def faltante(lista):
    """ """
    lista.sort()
    atual = []
    proximo = []
    cont = 1
    for i in lista:
        if lista[cont] == i:
            cont += 1
        else:
        	cont = i
            break
    return cont