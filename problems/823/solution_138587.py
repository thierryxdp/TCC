def faltante(lista):
    """"
    Está função determina o número inteiro que está faltando 
    em um determinado intervalo. Dada a lista com N-1 números inteiros 
    numerados de 1 a N.
    Parametro de entrada: list 
    Valor de Retorno: int
    """
    list.sort(lista)
    if 1 not in lista:
        return 1
    if lista[-1] < len(lista) + 1:
        return len(lista) + 1
    i = 0
    f = 0
    while i < len(lista) - 1:
        if lista[i + 1] - lista[i] > 1:
            f= f + lista[i] + 1
        i = i + 1
    return f