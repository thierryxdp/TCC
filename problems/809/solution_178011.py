def intercala(lista1, lista2):
    """Função que, dadas as listas, 1 e 2, de tamanho 3, gera uma lista L3 que
    é formada intercalando os elementos da lista 1 com os da lista 2;
    list,list->list"""
    soma1 = lista1 [0:1] + lista2 [0:1]
    soma2 = lista1 [1:2] + lista2 [1:2]
    soma3 = lista1 [2:] + lista2 [2:]
    return soma1 + soma2 + soma3