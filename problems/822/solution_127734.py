def repetidos(lista):
    x=0
    i=o
    while i<len(lista):
        if lista[i]==lista[i-1]:
            x=x+1
            x=i+1
            return x