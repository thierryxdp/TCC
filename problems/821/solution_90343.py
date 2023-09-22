def fatorial(n):
    """Funcao que recebe um numero n e retorna o fatorial dele. int=>int"""
    x = 1
    listadefatores = [ ]
    while x < n+1:
        listadefatores = listadefatores + [x,]
        x = x + 1
        
    i = 0
    p = 1
    while i < len(listadefatores):
        p = p*(listadefatores[i])
        i = i + 1
    return p