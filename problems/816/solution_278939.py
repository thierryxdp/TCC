def maiores(lista, n):
    lista2=[]
    i=0 
    while(i<len(lista)-1):
        if n<lista[i]:
            lista2.append(lista[i])
    return lista2