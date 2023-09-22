def qtd_divisores(n):
    """ A funçao qtd_divisores conta quantos divisores o número inserido tem,
    int --> int"""
    
    resultado = 0
    for i in range(1,n+1):
        if n%i == 0:
            resultado = resultado + 1

    return resultado