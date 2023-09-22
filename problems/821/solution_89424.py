def fatorial(numero):
    """Retorna o fatorial do numero escolhido;
    	int -> int"""
    f = 1
    while numero > 1:
        f = f*numero*(numero-1)
        numero = numero - 2
    return f