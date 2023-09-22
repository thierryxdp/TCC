def insere(lista_numero, n):
    '''retorna uma lista na ordem crescente
    list, int -> list'''
    n = int(n)
    lista_numemro = int(lista_numero)
    lista = list.extend(lista_numero, n)
    return  list.sort(lista)