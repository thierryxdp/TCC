def insere (lista_numero, n):
    """Insere n na posição correta dentro da lista de números ordenada em ordem crescente. lista, int -> lista"""
    l1 = list.append(lista_numero, n)
    lista =list.sort(l1)
    return lista