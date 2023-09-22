def insere(lista_num,n):
    '''Função que dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta, ou seja, de tal maneira que a lista continue
ordenada; list->list.'''
    if n not in lista_num:
        list.append(lista_num,n)
    list.sort(lista_num)
    indice= list.index(lista,n)

    fatiado= lista[indice+1:]
    return fatiado