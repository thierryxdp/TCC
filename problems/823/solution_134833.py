def faltante(lista):
    '''função que retorna a peça faltante; list -> int'''
    list.sort(lista)
    i = 1
    while i < len(lista):
        if not lista[i - 1] == lista[i] - 1:
            return i + 1
        i = i + 1
    if lista[0] != 1:
        return 1
    else:
        return lista[-1] + 1