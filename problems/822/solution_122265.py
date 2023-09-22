def repetidos(lista):
    i=0
    lista1=list.sort(lista)
    while i<len(lista):
        i=i+1
        if lista1[i+1]==lista1[i]:
        return i