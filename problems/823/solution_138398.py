def faltante(lista):
    """Função que, dada uma lista com N - 1 inteiros
    numerados de 1 a N, descobre qual o número inteiro
    deste intervalo está faltando.
    list -> int"""
    list.sort(lista)
    if 1 not in lista:
        return 1
    if lista[-1] < len(lista) + 1:
        return len(lista) + 1
    i = 0
    falta = 0
    while i < len(lista) - 1:
        if lista[i + 1] - lista[i] > 1:
            falta = falta + lista[i] + 1
        i = i + 1
    return falta