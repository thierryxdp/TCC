def faltante(lista):
    """Dada uma lista com N-1 inteiros numerados de 1 a N, descobre qual número desse intervalo está faltando
    list -> int"""
    y = 0
    if len(lista) == lista[-1]:
        return lista[-1] + 1
    else:
        while lista[y] == y + 1:
            y = y + 1
        return y + 1