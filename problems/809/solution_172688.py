def intercala(lista1, lista2):
    """Função que recebe duas listas L1 e L2 de tamanho 3 e retorna uma lista L3 formada intercalando os elementos de L1 e L2; list -> list """
    return [int(str(lista1[0:1])),int(str(lista2[0:1])),int(str(lista1[1:2])),int(str(lista2[1:2])), int(str(lista1[2:3])), int(str(lista2[2:3]))]