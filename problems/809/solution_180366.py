def intercala(lista1, lista2):
    """Funçao que dadas 2 listas de tamanho 3, gera uma terceira
    lista que é formada intercalando os elementos das duas primeiras
    list[int], list[int]-> list[int]"""
    in_list1 = lista1[::2]
    in_list2 = lista2[1::2]
    intercalada= in_lista1 + in_lista2
    return list(intercalada)