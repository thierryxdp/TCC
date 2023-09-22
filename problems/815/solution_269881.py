def insere(lista_numero, n):
    '''Função recebe uma lista e um termo e retorna esse termo
    dentro da lista em ordem crescente
    list, int -> list'''
    list.extend(lista_numero, [n])
    list.sort(lista_numero)
    return lista_numero