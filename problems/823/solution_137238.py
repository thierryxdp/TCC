def faltante(lista):
    """"
    Está função determina o número inteiro que está faltando 
    em um determinado intervalo. Dada a lista com N-1 números inteiros 
    numerados de 1 a N.
    list => int
    """
    list.sort(lista)
    i = 0
    falta = 0
    while i < len(lista) - 1:
        if lista[i + 1] - lista[i] > 1:
            falta = falta + lista[i] + 1
        i = i + 1
    return falta