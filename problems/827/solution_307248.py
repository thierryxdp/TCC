def qtd_divisores(numero):
    """Dado um número qualquer, retorna a quantidade de divisores
    que o número possui:
    int-->int"""
    divisores=0
    for n in range(1,numero+1):
        if numero%n==0:
            divisores+=1
    return divisores