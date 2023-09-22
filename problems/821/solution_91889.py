def fatorial(numero):
    """funcao que dado um numero calcula o seu fatorial;
    int -> int"""
    n = 1
    while numero > 0:
        n *= numero
    	numero = numero - 1
    return n