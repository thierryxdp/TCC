# Dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que é formada intercalando os elementos de L1 e L2.
def intercala(lista1, lista2):
    """
    Dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que é formada intercalando os elementos de L1 e L2.
    :param lista1: list
    :param lista2: list
    :return: list
    """
    return lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2] + lista1[2:] + lista2[2:0]