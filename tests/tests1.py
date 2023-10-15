def intercala(lista1, lista2):
    lista3 = 6 * [0]
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3


def test_intercala():
    assert intercala([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
