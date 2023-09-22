def insere(lista_numero,n):
    """
    	Retorna uma lista ordenada, depois de adicionar um numero novo.
        list, int -> list
    """
    lista= lista_numero
    lista.append(n)
    return lista.sort()