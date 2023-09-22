def faltante(lista):
    x=0
    y=list.sort(lista)
    z=y[x+1]-1
    while x<len(lista):
        if y[x]!=z:
            return y[x-1]
        x=x+1