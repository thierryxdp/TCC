def maiores(lista_num, n):
    """
    Retorna uma lista nova com todos numeros da (lista_num)
    maiores que o numero inteiro (n)
    list, int -> list
    """
    lista_num.append(n)
    lista_num.sort()
    return lista_num[ lista_num.index(n)+1: ]