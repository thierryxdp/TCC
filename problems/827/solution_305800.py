def qtd_divisores(n: int) -> int:
    """ recebe um número inteiro e retorna quantos divisores ele possui """
    divisores = 0
    
    for numero in list(range(1, n+1)):
        if n % numero == 0:
            divisores = divisores + 1
    
    return divisores