def faltante(lista):
    """função que recebe uma lista de números inteiros 
    numerados de 1 a N e retorna o número faltante dentro
    desse intervalo.
    list -> int"""
    lista.sort()
    N = lista[-1]
    sequencia = list(range(1, N+1))
    i = 0

    while i < len(lista):
        if sequencia[i] == lista[i]:
            falta = lista[-1] + 1
        else:
            falta = lista[i] - 1
            break
        i = i + 1
        
    return falta