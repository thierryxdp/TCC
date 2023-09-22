def repetidos(lista):
    y=0
    x=0
    while y<=len(lista):
        if lista[y]==lista[y+1]:
            x+1
        y+1
    return x