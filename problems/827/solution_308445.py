def qtd_divisores(n):
    """Dado um número, retorna quantos divisores o mesmo possui"""
    divisores = []
    for numero in range(1,n+1):
        if n%numero == 0:
            list.append(divisores,1)
    return sum(divisores)