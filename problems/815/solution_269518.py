def insere(l, n):

    """funcao que recebe uma lista ordenada e um numero inteiro e insere o numero na lista sem tirar a ordem"""

    #list, int -> list
    l.insert(0,n)
    list.sort(l)
    return l