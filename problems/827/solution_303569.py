def qtd_divisores(n):
    divisores=[n]
    lista=list(range(n))[1:]

    for x in lista:
        if n%x==0:
            divisores=divisores+[x]
            
   

    return len(divisores)