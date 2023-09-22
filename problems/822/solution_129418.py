def repetidos(lista):
    a=0
    i=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            a=a+1
    return a