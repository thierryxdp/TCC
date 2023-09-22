def maiores(lista_n_int, n):
    """
    int,int->list
    :param lista_n_int: Recebe lista com numeros inteiros
    :param n: Recebe um numero inteiro qualquer
    :return: Retorna uma nova lista com os numeros inteiros maiores que n
    """
    lista_maior_q_n = []
    for x in range(len(lista_n_int)-1):
        if lista_n_int[x] > n:
            lista_maior_q_n.append(lista_n_int[x])
    return lista_maior_q_n