def repetidos(lista):
    i=0
    lista1=list.sort(lista)
    while i<len(lista):
        if lista1[i+1]==lista1[i]:
        i=i+1
        return i