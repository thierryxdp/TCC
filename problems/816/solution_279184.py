def maiores(lista,n):
    x=[]
    z=-1
    teste = -1
    aux = -1
    for y in lista:
        z+=1
        if n < lista[z]:
        	x.append(y)
	x.sort()
    return x