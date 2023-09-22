def soma_h(n):
    """calcula e retorna o valor de h com n termos;
    int, float->"""
    
    h = 0
    i = 1
    while i == n:
        h = h + 1/i
        i = i + 1
    return h