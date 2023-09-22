def faltante(lista):
    x=0
    y=list.sort(lista)
    z=y[x+1]-1
    while x<len(lista):
        if z==y[x]:
            return y
        x=x+1