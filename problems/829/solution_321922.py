def soma_h(N: int) -> float:
    """comentário"""
    soma = 0
    for i in list(range(1,N+1)):
        soma += 1/i
    
    return round(soma,2)