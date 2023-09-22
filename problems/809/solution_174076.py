def intercala(lista1, lista2):
    """Dadas duas listas L1 e L2, gera uma lista L3 com os elementos intercalados de L1 e L2"""
    lista3 = []
    for *a,*b in zip(lista1, lista2):
        lista3.append(*a)
        lista3.append(*b)
        return lista3