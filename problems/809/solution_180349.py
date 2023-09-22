def intercala(lista1, lista2):
    """Funçao que dadas 2 listas de tamanho 3, gera uma terceira
    lista que é formada intercalando os elementos das duas primeiras
    list[int], list[int]-> list[int]"""
    len(lista1)=3
    len(lista2)=3
    return [lista1[::2]+ lista2[1::2]