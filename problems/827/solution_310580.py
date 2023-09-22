def qtd_divisores(x):
    """funcao que conta quantos divisores um numero tem e retorna eles"""
    divisores = 0
    for i in range(1, x+1):
        if x % i == 0:
            divisores += 1
            
    return divisores