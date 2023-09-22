def soma_h(N: int)-> float:
    """Dado um número inteiro N, calcula e retorna a soma de
    parte da série harmônica delimitada por N.
    
    A série harmônica tem como termo geral 1/n, com n variando
    de 1 a infinito. A função 'corta' a série em n = N."""
    
    soma = 0
    for numero in range(1,N + 1):
        soma += 1 / numero
        
    return round(soma,2)