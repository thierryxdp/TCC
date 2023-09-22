def insere(lista_numero,n):
    """
    	Retorna uma lista ordenada, depois de adicionar um numero novo.
        list, int -> list
    """
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero