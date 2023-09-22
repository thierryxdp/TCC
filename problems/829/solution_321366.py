def soma_h(n):
    """calcula e retorna o valor de h com n termos;
    int, float->"""
    
    h = 0
    for i in range(n):
        
        h = h + 1/i
    return h