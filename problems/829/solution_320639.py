def soma_h(x):
    """Dado um numero inteiro, retorna a soma gerada por (1/1)+(1/2)...+(1/x)"""
    """entrada: int
    saida: float"""
    
    soma = 0
    
    for pos in range(1,x+1):
        divisao = 1/pos
        soma = soma + divisao
        
    return round(soma,2)