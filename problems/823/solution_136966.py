def faltante(lista):
    x=0
    y=1
    while x<len(lista)-1:
        if lista[x]!=y:
            return y
        x+=1
        y+=y
    return len(lista)+1