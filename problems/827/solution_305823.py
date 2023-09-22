def qnt_divisores(n:int):
    """Função que dado um número de entrada, calcula quantos
       divisores o número tem."""
    divisores = 0
    for i in range(1,n+1):
        if n % i == 0:
            divisores = divisores + 1 
    return divisores