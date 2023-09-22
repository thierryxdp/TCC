def qtd_divisores(n):
    
    lista = list(range(1,n))
    i=0
    L = []
    
    for e in lista:
        if (n%lista[i])==0:
            list.append(L,lista[i])
            list.count(L,lista[i])
        i+=1
    return list.count(L,lista[i])