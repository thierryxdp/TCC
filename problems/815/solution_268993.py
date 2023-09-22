def insere(lista_numero,n):
    """
    Insere um numero numa lista na posicao correta, ordem crescente
    Parametros:
    	lista_numero -> list
        a lista em que deve ser inserido o numero
        n -> int
        numero a ser inserido na lista
    Returns:
    	list
        nova lista com o numero inserido
    """
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero