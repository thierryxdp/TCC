def intercala(lista1, lista2):
    """Dadas duas listas L1 e L2, gera uma lista L3 com os elementos intercalados de L1 e L2"""
    lista3 = []
    for a,b,c,d,e,f in zip(lista1, lista2):
        lista3.append(a)
        lista3.append(b)
        lista3.append(c)
        lista3.append(d)
        lista3.append(e)
        lista3.append(f)
        return lista3