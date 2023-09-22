def soma_h(n: int) -> float:
    """Calcula e retorna o valor H com N termos.
    Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
    Obs: O resultado será retornado com 2 casas decimais"""
    
    h = []
    for i in range(1, n + 1):
        list.append(h, 1/n)
    return sum(h)