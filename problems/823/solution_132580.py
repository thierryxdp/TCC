def faltante(N):
    '''função que retorna numero faltante de uma sequencia de numeros
    lista -> int'''
    i = 0
    x = 1
    faltante = N[i] + 1
    while x < len(N):
        list.sort(N)
        if N[x] - N[i] != 1:
            faltante = faltante + N[i]
        i = i + 1
        x = x + 1
    return faltante