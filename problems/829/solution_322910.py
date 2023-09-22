def soma_h(n):
    """
    Função que calcula o valor de h, de acordo com a fórmula dada.
    int -> float
    """
    
    divisores = list(range(1,n+1))
    
    for elemento in divisores:
        soma_h = (1/divisores) 
        soma_total = 1 + soma_h
        
    return round(soma_total,2)