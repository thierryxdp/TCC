def soma_h(n):
    """Funcao que calcula a soma de n termos sobre 1;
    int -> float"""
    
    soma = 0
    
    for i in range(1,n+1):
        soma += 1/i
    
    return round(soma, 2)