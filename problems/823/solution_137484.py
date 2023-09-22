def faltante(lista):
    i=1
    while i<=len(lista)+1:
        if lista[i-1]==i:
            i+=1
        else:
            return i