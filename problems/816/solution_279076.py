def maiores(lista,n):
    x=[]
    z=-1
    for y in lista:
        z+=1
        if n < lista[z]:
        	x.append(y)
    return x