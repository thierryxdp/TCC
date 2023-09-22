def filtra_pares(t):
    '''
        Função responsável por analisar uma lista e filtrar os valores pares dela.
        t: Tupla com valores numéricos
        Saída: Tupla  => Tupla
    '''
    t = list(t)
    pares = []
    for i in t:
        if(i % 2 == 0):
            pares.append(i)
    return tuple(pares)