def filtraMultiplos(lista_numeros, n):
    """
    	Funcao que recebe uma lista de numeros e um numero.
        Retorna uma nova lista com todos os elementos da lista recebido, porém divisiveis por n;
        list, int -> list
    """
    lista_divisivel_n = []
    for numero in lista_numeros:
        if numero % n == 0:
            lista_divisivel_n.append(numero)
    return lista_divisivel_n