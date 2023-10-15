def intercala(lista1, lista2):
    lista3 = 6 * [0]
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3


def test_intercala_2():
    assert intercala([7, 9, 11], [8, 10, 12]) == [7, 8, 9, 10, 11, 12]
