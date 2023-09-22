def qtd_divisores(n):
    lista_num=list(range(1,n+1))
    divisores=0
    
    for i in lista_num:
        if n%i==0:
            divisores=divisores+1
    return divisores