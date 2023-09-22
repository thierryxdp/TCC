def fatorial(numero):
    """
    	Função que calcula o fatorial de um número.
        int ->
    """
    fato = 1
    while numero!=0:
        fato = fato*numero
        numero = numero - 1
    return fato