def soma_h(N: int) -> float:
    """comentário"""
    soma = [1]
    for i in list(range(1,N+1)):
        soma += [1/N,]
    
    return soma