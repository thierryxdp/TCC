def intercala(lista1:list, lista2:list)->list:
    """Dadas duas listas com 3 elementos, retorna uma terceira lista com 6 elementos, originada da intercalação entre as duas primeiras."""
    return list((lista1[0],)+(lista2[0],)+(lista1[1],)+(lista2[1],)+(lista1[2],)+(lista2[2],))