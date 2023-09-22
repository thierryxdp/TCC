def insere(lista_numero,n):
    '''Função que, dada uma lista ordenada, insira o número n na lista de forma que continue ordenada.
list, int --> list'''
    lista_mais_n = lista_numero + [n]
    list.sort(lista_mais_n)
    return lista_mais_n