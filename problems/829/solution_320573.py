def soma_h(n):
    """Calcula o valor da soma dados n termos.
       int -> int"""
    
    soma = 0
    
    for i in range(1,n+1):
        soma += 1.0 / i
        
    return round(soma,2)