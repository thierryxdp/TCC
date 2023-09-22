def insere(lista_numero,n):
    """ Insere um numero de entrada, n, em uma lista em ordem
    list,int -> list """
    list.append(lista_numero,n) #Insere o numero na lista
    list.sort(lista_numero)# Ordena na lista
    return lista_numero # Retorna a lista com n