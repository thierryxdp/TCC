def soma_h(n):
    """recebe um numero inteiro n e retorna o somatorio de 
    H = 1/1 + 1/2 + ... 1/n
    int -> float"""
    
    h = 0
    
    for i in range(1, n + 1):
        h += 1 / i
        
    return h