def qtd_divisores(n):
    """"""
    """"""
    divisores=0
    lista = list(range(1,n+1))
    for elemento in lista:
        if elemento%n==0:
            divisores=divisores+1
    return divisores