def qtd_divisores(n):
    """funcao que calcula a quantidade de divisores de um determinado numero;int->int"""
    divisores=0
    for i in list(range(1,n+1)):
        if n%list(range(1,n+1))[i]==0:
            divisores=divisores+1
    return divisores