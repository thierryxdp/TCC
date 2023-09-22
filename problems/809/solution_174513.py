def intercala(lista1, lista2):
    """Função que dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que é formada intercalando os elementos de L1 e L2.
    (list, list) -> list"""

    return [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]