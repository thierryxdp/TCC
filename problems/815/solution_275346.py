def insere (lista_numero, n):
    """Insere n na posição correta dentro da lista de números ordenada em ordem crescente. lista, int -> lista"""
    lista = list.append(lista_numero, n)
    lista2 = list.sort(lista)
    return lista2