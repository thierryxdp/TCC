def faltante(lista):
    x=list(range(1,len(lista)+3,))
    y=0
    z=0
    while y<=len(lista):
        if x[y] not in lista:
            z=z+x[y]
        y=y+1
    return z