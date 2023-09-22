def insere(lista_numero, n):
    '''retorna uma lista na ordem crescente
    list, int -> list'''
    n = int(n)
    return  list.sort(list.extend(lista_numero,n))