def intercala(lista1, lista2):
    L3 = Lista1+Lista2
    L3[::2] = Lista1
    L3[1::2] = Lista2
    return L3