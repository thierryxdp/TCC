def insere(lista_numero,n):
    """Dado um numero n e uma lista  de numeros ordenada de forma crescente,
    retorna-se uma lista tambem ordenada (crescente) com o numero n incluso
    Entradas:
    	lista_numero -> lista
        n -> int
    Returns: lista"""
    lista_numero2 = lista_numero + [n]
    lista_final = list.sort(lista_numero2)
    return lista_final