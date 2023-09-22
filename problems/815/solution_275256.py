def insere (lista_numero,n):
    '''Função em que dada um lista ordenada (crescente) de números inteiros e
    um número inteiro (n), inclua o número na posição correta, ou seja, mantendo a
    lista ordenada;
    list, int -> list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero