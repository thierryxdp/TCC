def intercala(lista1:list, lista2:list)->list:
    """Dadas duas listas com 3 elementos, retorna uma terceira lista com 6 elementos, originada da intercalação entre as duas primeiras."""
    return list(tuple(lista1[0])+tuple(lista2[0])+tuple(lista1[1])+tuple(lista2[1])+tuple(lista1[2])+tuple(lista2[2]))