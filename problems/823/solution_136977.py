def faltante(lista):
    x=0
    y=1
    while x+1<len(lista):
        if lista[x]!=y:
            return y
        else:
        	x+=1
        	y+=y
    return y+1