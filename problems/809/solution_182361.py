def intercala(lista1, lista2):
    r=lista1+lista2
    r[::2]=lista1
    r[1::2]=lista2
    return r