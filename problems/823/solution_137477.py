def faltante(lista):
    i=1
    while i<len(lista):
        if lista[i]==i:
            i+=1
        else:
            return i