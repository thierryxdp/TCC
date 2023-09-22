def fatorial(numero):
    """calcula o fatorial do numero dado.
    entrada e saída: int"""
    i = 1
    while(numero>1): 
        i = i * numero 
        numero = numero - 1
    return i