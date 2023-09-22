def faltante(lista):
    x=0
    y=list.sort(lista)
    
    while x<len(lista):
        if y[x]!=len(lista)+1:
            return len(lista)+1
        x=x+1