def soma_h(N:int) -> float:
    """Função que, dado um número inteiro N, retorna
    o valor de H, que é (1 + 1/2 + 1/3 + ... + 1/N)."""
    
    soma = 0
    
    for numero in range(1,N+1):
        soma += 1/numero
    
    return round(soma,2)