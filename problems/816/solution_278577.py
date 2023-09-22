def maiores(lista, n):
    """
    int,int->list
    :param lista: Recebe lista com numeros inteiros
    :param n: Recebe um numero inteiro qualquer
    :return: Retorna uma nova lista com os numeros inteiros maiores que n
    """
    listaMaior = []
    for el in lista:
        if el > n:
            listaMaior.append(el)
    return listaMaior.sort()