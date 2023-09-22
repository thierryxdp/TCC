def soma_h(n):
    """essa funcao, dado um numero inteiro n como entrada, calcula e retorna o valor H
    H = 1+1/2+1/3+... +1/n
    int -> float"""
    
    H = 0
    
    for x in range(1,n+1):
        H += 1/x
    
    return round(H,2)