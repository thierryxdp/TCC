def faltante(lista):
    cont = 0
    while cont < len(lista):
        lista.sort()
        if lista[cont]-lista[cont-1]>1:
            return lista[cont-1]+1
    return lista