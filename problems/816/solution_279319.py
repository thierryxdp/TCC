def maiores(lista_int,n):
    """Função que retorna uma lista com todos os elementos de uma lista
dada que forem maiores no que o inteiro n"""
    list.sort(lista_int)
    x = list.count(lista_int,n)
    if x > 0:
       z = list.index(lista_int,n)
       if z == 0:
        return lista_int[1:len(lista_int)]
       elif z == len(lista_int):
            return []
        else:
           return lista_int[n:len(lista_int)]
    if x == 0:
        if (lista_int[0]) > n:
            return lista_int
        else:
            return []