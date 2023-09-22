def intercala(lista1, lista2):
    """Função que recebe duas listas L1 e L2 de tamanho 3 e retorna uma lista L3 formada intercalando os elementos de L1 e L2; list -> list """
    return [int(lista1[0:1]),int(lista2[0:1]),int(lista1[1:2]),int(lista2[1:2]), int(lista1[2:3]), int(lista2[2:3])]