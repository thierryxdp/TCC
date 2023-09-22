def insere(lista_numero, n):
    ''' Essa função recebe uma lista ordenada de forma crescente com números
    inteiros e um número inteiro n, e retorna a lista com o número n de forma
    que ela continue ordenada;
    list,int->list. '''
    lista_nova = lista_numero + [n]
    list.sort(lista_nova)
    return lista_nova