def intercala(lista1, lista2):
    """Dadas duas listas L1 e L2, gera uma lista L3 com os elementos intercalados de L1 e L2"""
    assert len(lista1)==len(lista2)
    n = len(lista1)
    intercalada = []
    for i in range(n):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])
        return intercalada