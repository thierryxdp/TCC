def faltante(lista):
    cont = 0
    while cont < len(lista):
        if lista[cont]-lista[cont-1] > 1:
            lista.sort()
            return lista[cont]-1
    return lista