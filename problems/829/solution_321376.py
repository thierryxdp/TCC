def soma_h(n):
    """calcula e retorna o valor de h com n termos;
    int, float->"""
    
    h = 1
    i= 2
    while i == n:
        h = h + 1/i
        i = i + 1
        return round(h, 2)