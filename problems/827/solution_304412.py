def qtd_divisores(n):
    """Calcula e retorna quantos divisores determinado numero tem"""
    divisores = 0
    for numero in range(1,n+1):
        if n%numero == 0:
            divisores += 1
    return divisores