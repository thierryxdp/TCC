def intercala(lista1, lista2):
    """Recebe duas listas de tamanho 3, L1 e L2 e retorna uma lista L3 com elementos intercalados de L1 e L2"""
    l3 = lista1[0] + lista2[0] + lista1[1] + lista2[1] + lista1[2] + lista2[2]
    return l3