def faltante(lista):
    x=0
    y=1
    while x<len(lista):
        if lista[x]==y:
            x+=1
        	y+=y
            
        else:
        	return y+1
    return y+1