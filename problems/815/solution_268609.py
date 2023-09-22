def insere(lista_numero,n):
    """ dada uma lista ordenada(crescente) de números inteiros e um número
    inteiro n, inclui n na posição correta (de tal maneira que a lsta continue
    ordenada).
    list,int -> list """
    a = list.append(lista_numero,n)
    b = list.sort(a)
    return b