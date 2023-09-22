def faltante(lista_n):
    """
    	Funcao que recebe um lista n - 1 ordenado de 1 a N.
        Retorna o numero que falta esta faltando.
        list -> int
    """
    lista_correta = list(range(1, len(lista_n) + 1))
    for (i, n) in enumerate(lista_n):
        if n != lista_correta[i]:
            return lista_correta[i]
	
    return len(lista_n) + 1