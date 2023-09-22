def soma_h(n):
    """Recebe um número e retorna essa soma.
    int -> float"""
    
    soma = 0
    
    for i in range(1, n+1):
        a = 1/i
        soma += a
    return soma