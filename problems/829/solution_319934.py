def soma_h (N):
    """Função que, dado um número N inteiro, retorna o resultado de H. A fórmula de H é: H = 1 + (1/2) + (1/3) + (1/4) + ... + (1/N).
    entrada: int
    saída: int"""
    
    resultado = 0
    lista = list(range(1,N+1))
    
    for numero in lista:
        resultado = resultado + (1/numero)
        
    return resultado