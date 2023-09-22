def insere(lista_numero, n):
    '''Faça uma função que dada uma lista ordenada inclua n na posição correta, list -> list'''
    ordem = [lista_numero, n]
    list.sort(ordem)
    return ordem