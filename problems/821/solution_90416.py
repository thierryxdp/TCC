def fatorial(numero):
    """dado um numero retorna o fatorial dele"""
    
    i = numero - 1
    while i > 0:
        numero *=i
        i-=1
    return numero