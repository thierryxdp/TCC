def insere(lista_numero, n):
    """ Inclui o número n em uma posição da lista de forma que ela permaneça ordenada.
    	list, int -> list
        
        Parameters:
        lista_numero: Lista
        n: Número n
        
        Returns:
        Lista contendo o número n e ordenada em ordem crescente.
    """
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero