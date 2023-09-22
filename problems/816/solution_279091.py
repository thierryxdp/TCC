def maiores(lista,n):
    x=[]
    z=-1
    teste = -1
    aux = -1
    for y in lista:
        z+=1
        if n < lista[z]:
        	x.append(y)
    for y in x:
        aux +=1
        for z in x:
            teste += 1
            if y > z:
                x.pop(teste-2)
                x.insert(aux,z)
    return x