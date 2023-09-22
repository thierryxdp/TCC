def soma_h(n):
    """calcula e retorna o valor de h com n termos;
    int, float->"""
    
    h = 0
    for (i=1; i<=n; i++):
        h = h + 1/i
        i = i + 1
    return h