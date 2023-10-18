# def intercala(lista1, lista2):
#     lista3 = 6 * [0]
#     lista3[::2] = lista1
#     lista3[1::2] = lista2
#     return lista3


def intercala(lista1, lista2):
    for e1 in lista1:
        print("a")
        lista2.append(e1)
    for e2 in lista2:
        print("b")
        lista1.append(e2)
    return lista1
