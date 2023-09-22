def maiores(lista, n):
    """função recebe lista e número inteiro e retorna
    lista com elementos da entrada a partir do número inteiro"""
    if n in lista:
        list.sort(lista)
        lista1 = lista[list.index(lista, n) + 1:]

        return lista1
    
    else:
        lista.insert(-1, n)
        list.sort(lista)
        lista1 = lista[list.index(lista, n) + 1:]

        return lista1