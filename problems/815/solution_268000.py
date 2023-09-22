def insere(lista_numero, n):
    ''' função com entradas para uma lista de números inteiros em
        ordem crescente e um número inteiro, respectivamente,
        retornando um nova lista, com o número indicado sendo um
        novo elemento da lista inical mantendo a ordem crescente
        [list, int-->list]'''
    A = lista_numero + [n]
    list.sort(A)
    return A