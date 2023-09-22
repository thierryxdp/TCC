def filtraMultiplos(lista_numero, n):
    '''Função que retorne uma nova lista contendo todos os elementos da lista divisíveis por n, list, int -> list'''
    x = 0
    listanum = []
    while x<len(lista_numero):
        if lista_numero[x]%n == 0:
            listanum.append(lista_numero[x])
        x = x + 1
    return listanum