def repetidos(lista):
    h=0
    i=0
    while i<len(lista):
        if lista[i]==lista[i+1] or lista[i+1]==lista[i+2]:
            h=h+1
        i=i+2
    return h