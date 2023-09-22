def faltante(lista):
    x=0
    y=list.sort(lista)
    
    while x<len(lista):
        if y[x]==y[x-1]+1:
            x=x+1
        return x