def insere(lista_numero,n):
    '''
    Dado uma lista ordenada (crescente) de numeros inteiros e um numero inteiro n,
    inclua na posicao correta e ordenada.

    Uso:
    insere(lista_numero,n)

    Entrada:
    - lista (list, int): Lista de falta dos times

    Saída:
    - Retorna uma nova lista ordenada em ordem crescente. (lista, int)
    '''

    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    return lista_numero