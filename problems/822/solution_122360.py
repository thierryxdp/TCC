def repetidos(lista):
    i=0
    iea=0
    while i<len(lista):
        if lista[i] == lista[i-1]:
            iea=iea+1
        i=i+1
    return iea