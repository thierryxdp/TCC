def insere(lista_numero, n):
    '''retorna uma lista na ordem crescente
    list, int -> list'''
    lista_numero = list.extend(lista_numero, n)
    lista_crescente = list.sort(lista_numero)
    return lista_crescente