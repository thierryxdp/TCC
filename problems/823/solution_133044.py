def faltante(lista):
    k = 0
    lista.sort()
    lista_default = range(1, lista[-1])
    for i in lista:
        if i not in lista_default:
            k = i
    return k