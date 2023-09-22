def faltante(lista):
    '''função que retorna a peça faltante; list -> int'''
    list.sort(lista)
    i = 1
    while i < len(lista):
        if not lista[i - 1] == lista[i] - 1:
            return i
        i = i + 1