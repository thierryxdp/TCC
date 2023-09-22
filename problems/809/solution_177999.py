def intercala(lista1, lista2):
    L3 = lista1+lista2
    L3[::2] = lista1
    L3[1::2] = lista2
    return L3