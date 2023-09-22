def qtd_divisores(n):
    
    lista = list(range(1,n+1))
    i=0
    L = []
    
    
    for e in lista:
        if (n%lista[i])==0:
            list.append(L,lista[i])
            d=list.count(L,int)
        i+=1
    return d