def faltante(lista):
    i=1
    while i<len(lista):
        if lista[i-1]==i:
            i+=1
        elif lista[i-1]!=i:
            return i