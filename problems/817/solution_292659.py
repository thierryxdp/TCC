def acima_da_media(lista):
    """ Dada uma lista com todas as notas, retorna as que ficaram acima da média.
    	list -> list
        
        Parameter:
        lista: Lista com todas as notas.
        
        Returns:
        Lista com as notas que ficaram acima da média.
    """
    media = sum(lista) / len(lista)
    list.sort(lista)
    while len(lista) > 0 and lista[0] <= media:
        del lista[0]
    return lista