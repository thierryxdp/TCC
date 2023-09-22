def maiores(lista_numero,n):
    '''Ao receber uma lista numérica ordenada, recebe também um número n e
insere n na lista na ordem correta e retorna uma nova lista com o pedaço
da lista com os elementos maiores que n. list, int --> list'''
    lista = lista_numero[:]
    list.append(lista,n)
    list.sort(lista)
    return lista[int(list.index(lista,n))+1:]