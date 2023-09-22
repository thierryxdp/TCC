def insere(lista_numero,n):
    '''Função que dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta, ou seja, de tal maneira que a lista continue
ordenada; list->list.'''
    if n not in lista_numero:
        list.append(lista_numero,n)
    list.sort(lista_numero)
    indice= list.index(lista_numero,n)

    fatiado= lista_numero[indice+1:]
    return fatiado