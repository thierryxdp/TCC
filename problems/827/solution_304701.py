def qtd_divisores(n):
    """Retorna o número de divisores inteiros possíveis, dado: n(um numero
     inteiro"""
    div = 0
    for i in range(1, n+1):
        if n % i == 0:
            div += 1
    return div