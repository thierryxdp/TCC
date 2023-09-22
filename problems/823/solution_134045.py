def faltante(lista):
    '''Recebe uma lista com os números de cada peça do quebra-cabeças
    menos a peça faltante e informa qual é a peça faltante; list -> int'''
    list.sort(lista)
    f = lista[-1]
    a = []
    i = 1
    while i <= f:
        a = a + [i]
        i = i + 1
    k = 0
    while k < len(a):
        if lista[k] != a[k]:
            return (k + 1)
        k = k + 1
    return a[-1] + 1