def faltante(N):
    '''Dado uma lista de números N, retornará o número faltante dessa
    sequencia de numeros, sem o numero zero.(lista => int)'''

    N = N + [0]
    list.sort(N)
    i = 0
    x = 1
    faltante = (N[-1]) + 1

    while x < len(N):
        if N[x] - N[i] != 1:
            faltante = faltante - (N[-1]) + N[i]
        i = i + 1
        x = x + 1
        
    return faltante