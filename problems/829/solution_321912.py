def soma_h(N: int) -> float:
    """comentário"""
    soma = 1
    for i in list(range(N+1)):
        soma += (1/i)
    
    return soma