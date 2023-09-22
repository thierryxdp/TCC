def fatorial(numero):
    """A função retorna o fatorial do numero dado utilizando
	o comando while. int->int"""
    i = 1
    while numero>1:
        i = i * numero
        numero = numero - 1
    return i