def faltante(lista):
    x=0
    y=1
    while x<len(lista):
        if lista[x]!=y:
            return y+1
        else:
        	x+=1
        	y+=y
    return 100