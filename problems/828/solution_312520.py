def primo(n):
    """
    int->bool
    :param n: Entrada de um numero qualquer.
    :param return: Retorna um valor booleano verificando se é primo o número
    de entrada.
    """
    lista = range(2,n)
    e=0
    for count in lista:
        if (n%count)==0:
        	return False
    return True