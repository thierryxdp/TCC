def insere(lista_numero, n):
    '''retorna uma lista na ordem crescente
    list, int -> list'''
    n = int(n)
    lista_numero = list.extend(lista_numero, n)
    return  list.sort(lista_numero)