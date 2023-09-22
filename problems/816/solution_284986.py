def insere(lista_numero,n):
    '''funcao que recebe uma lista de numeros ordenada crescente e inclui um numero n de forma que
    continue ordenada. list -> list'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    '''recebe uma lista e um numero n, e retorna so os numeros maiores que n da lista em ordem crescente
    list, int -> list'''
    lista1 = insere(lista,n)
    lista1[:n] =
    return lista1