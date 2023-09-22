def qtd_divisores(n:int) -> int:
    """Função que, dado um número inteiro n,
    calcula a quantidade de divisores que
    ele tem."""
    
    numero_divisores = 0
    
    for divisor in range(1,n+1):
        if n % divisor == 0:
            numero_divisores += 1
        
    return numero_divisores