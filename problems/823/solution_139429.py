def faltante(lista):
    i=1
    if lista[0] is not 1:
        return 1
    while i<len(lista):
        if lista[i]not in lista:
            return lista[1]
        else:
            i=i+1