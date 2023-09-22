def faltante(lista):
    x=list(range([1],len(lista)+2,1))
    y=0
    z=0
    while y<len(lista):
        if lista[y] not in x:
            z=z+lista[y]
        y=y+1
    return z