def intercala(lista1, lista2):
    """Função que dada duas listas de 3 elementos, retorna uma nova lista
       intercalando os elementos da lista1 e da lista2.
       list,list->list
       
       Parâmetros:
       lista1: primeira lista que será intercalonada.
       lista2: segunda lista que será intercalonada.
       
       returns: Uma nova lista com os elementos de ambas as primeiras listas 
                intercalonadas.
    """
    return lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]