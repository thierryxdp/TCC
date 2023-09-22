def soma_h(N):
    """Calcular e retornar o valor de H com N termos.
    int --> float"""
    
    soma = 0
    
    for i in range(N+1):
        soma = soma + 1/i
    return round(soma,2)