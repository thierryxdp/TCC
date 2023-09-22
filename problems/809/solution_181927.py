def intercala(lista1, lista2):
    """dadas 2 listas de tamanho 3, gera uma lista que e formada intercalando os elementos de l1 e l2"""
    return [lista1[0],]+[lista2[0],]+[lista1[1],]+[lista2[1],]+[lista1[2],]+[lista2[2],]