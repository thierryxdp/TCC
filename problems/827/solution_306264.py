def qtd_divisores(n):
    '''Função que conta quantos divisoresum número tem.
    int->int'''
    
    lista = list(range(1,n+1))
    i=0
    L = []
    
    
    for e in lista:
        if (n%lista[i])==0:
            list.append(L,lista[i])
            
        i+=1
    return len(L)