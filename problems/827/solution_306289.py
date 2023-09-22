def qtd_divisores(n):
    """"""
    """"""
    divisores=0
    lista = list(range(1,n+1))
    for i in lista:
        if i%n==0:
            divisores=divisores+1
    return divisores