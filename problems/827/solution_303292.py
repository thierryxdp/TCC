def qtd_divisores(numero):
    """Retorna a quantidade de divisores de um numero. int-->int"""
    n=numero
    divisores=0
    while n>0:
        if numero%n==0:
            divisores=divisores+1
        n=n-1
    return divisores