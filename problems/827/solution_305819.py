def qtd_divisores(n: int)-> int:
    """Dado um número inteiro (n), a função retorna a quantidade de divisores
    que este número possui"""
    divisores = list()
    for numero in range(1, n+1):
        if (n % numero == 0):
            list.append(divisores, numero)
    return len(divisores)