#Start your python function here
def filtra_pares(a, b, c, d):
    '''Dada uma tupla com quatro elementos inteiros a, b, c e d, retorna uma nova tupla contendo apenas os elementos pares, na mesma ordem em que se encontravam na tupla original;
	assinatura: int, int, int, int --> tuple(...)
    Casos de teste:
    filtra_pares(1, 2, 3, 4) == (2, 4)
    filtra_pares(4, 3, 2, 1) == (4 ,2)
    filtra_pares(0, -5000, 199, 200) == (0, -5000, 200)'''
    [a, b, c, d] = lista
    for item in lista:
        if (item % 2) != 0:
            lista.remove(item)
    tupla = tuple(lista)
    return tupla