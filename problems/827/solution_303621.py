def qtd_divisores(n):
    divisores=[n]
    lista=list(range(n))[1:]
    
    if n<0:
        return 0
    else:
        
        for x in lista:
            if n%x==0:
                divisores=divisores+[x]
        return len(divisores)