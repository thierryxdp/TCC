def maiores(lista, n):
    lista2=[]
    lista3=[]
    k=0
    j=0
    for k in range(len(lista)):
            for j in range(k):
                if isinstance(lista[k], int):
                    lista3.append(lista[k][j])
    i=0 
    while(i<len(lista3)-1):
        if n<lista[i]:
            lista2.append(lista3[i])
        i+=1
    return lista2