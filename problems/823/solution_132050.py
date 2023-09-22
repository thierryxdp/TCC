def faltante(lista_n):
    """
    	Funcao que recebe um lista n - 1 ordenado de 1 a N.
        Retorna o numero que falta esta faltando.
        list -> int
    """
    return lista_n - list(range(1, len(lista_n) + 1))