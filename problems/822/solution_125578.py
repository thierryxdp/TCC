def repetidos(lista):
    i=0
    l=2
    while i<len(lista):
        if lista[i]==lista[i-1]:
            l=l+1
        i=i+1
        return l