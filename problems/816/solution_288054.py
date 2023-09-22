def maiores(lista_int,n):
    """A funçao gera uma lista com numeros maiores que n, dadas uma lista e n. list,int-->list """
    list.append(lista_int,n)
    list.sort(lista_int)
    s = list.index(lista_int,n)
    return lista_int[s+1:]