def soma_h(N: int) -> float:
    """Calcula e retorna o valor H com N termos.
    Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
    Obs: O resultado será retornado com 2 casas decimais"""
    
    H = []
    for i in range(1, N + 1):
        list.append(H, 1/i)
    return round(sum(H),2)