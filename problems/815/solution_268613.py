def insere(lista,n):
    """ dada uma lista ordenada(crescente) de números inteiros e um número
    inteiro n, inclui n na posição correta (de tal maneira que a lsta continue
    ordenada).
    list,int -> list """
    a = list.append(lista,n)
    return list.sort(a)