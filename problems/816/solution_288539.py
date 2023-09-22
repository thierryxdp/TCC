def maiores(lista, n):
    '''funcao recebe lista e numero inteiro, retornando lista com intens de entrada a partir do numero inteiro. list, int -->list'''
    if n in lista:
        list.sort(lista)
        lista1 = lista[list.index(lista,n) + 1:]
        return lista1
    else:
        lista.insert(-1, n)
        list.sort(lista)
        lista1 = lista[list.index(lista,n) + 1:]
        return lista1