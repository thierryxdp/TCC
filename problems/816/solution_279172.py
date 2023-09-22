def maiores(lista,n):
    x=[]
    z=-1
    teste = -1
    aux = -1
    for y in lista:
        z+=1
        if n < lista[z]:
        	x.append(y)
    count = 0
    count2 = 0
    while count < len(x):
        if x[count] < x[count2]:
            x.insert(count -1 ,x[count2])
            x.pop(count2-1)
            
            
            count = 0
            count2 = 0
        else:
            count +=1
            count2+=1
            
    return x