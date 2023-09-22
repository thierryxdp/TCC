def faltante(lista):
    x=0
    while x<=len(lista)-1:
        if lista[x]==lista[x]+1:
            x=x+1
 	return x+1