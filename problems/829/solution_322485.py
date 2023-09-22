import math
def soma_h (n):
    """Função que """
    """ """
    soma = 0
    for i in range (1, n+1):
        soma = soma + (1/(i*(i+1)))
    i = i + 1
    
    return soma

def erro (erro=0.01):
    n = 0 
    referencia = soma_h(n)
    
    while math.fabs(1-referencia)>erro:
        referencia = soma_h(n)
    return (referencia, n)