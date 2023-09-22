def intercala(lista1, lista2):
    """Funçao que dadas 2 listas de tamanho 3, gera uma terceira
    lista que é formada intercalando os elementos das duas primeiras
    list[int], list[int]-> list[int]"""
    intercalada= in_lista1 + in_lista2
    intercalada:[::2]= in_list1
    intercalada:[1::2]=in_list2
    return list(intercalada)