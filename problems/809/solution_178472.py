def intercala(lista1, lista2):
    """Esta função gera uma lista L3 intercalada pelos elementos de L1 e L2;
       list, list -> list"""
    lista3=lista1[:1]+lista2[:1]+lista1[1:3]+lista1[:2]+lista2[:2]+lista2[1:3]
    return lista3