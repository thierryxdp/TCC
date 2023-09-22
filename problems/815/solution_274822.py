def insere(lista_numero, n):
    '''retorna uma lista na ordem crescente
    list, int -> list'''
    lista_numero = list.extend(lista_numero, n)
    return  list.sort(lista_numero)