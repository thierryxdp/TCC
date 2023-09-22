def repetidos(lista):
    h=0
    i=0
    while i<len(lista):
        if lista[i]==lista[i+1]:
            h=h+1
        i=i+1
        else:
            i=i+1
        return h