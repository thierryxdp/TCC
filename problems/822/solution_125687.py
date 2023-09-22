def repetidos(lista):
    i=0
    while len(lista)>i:
        if lista[i]==lista[i]+1:
            i=i+1
        return i