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
        teste = 0
        aux +=1
        for z in x:
            teste += 1
            if y > z:
                x.pop(teste-1)
                x.insert(aux-2,z)
    for y in x:
        teste = 0
        aux +=1
        for z in x:
            teste += 1
            if y > z:
                x.pop(teste-1)
                x.insert(aux-2,z)
           
    return x