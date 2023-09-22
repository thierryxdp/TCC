def conta_frases(texto):
    #faz coisas
    ponto= str.count(texto,'.')
    ex = str.count(texto, '!')
    inter = str.count(texto, '?')

    if ('...' in texto != False):
        pontinhos = str.count(texto, '...')
        pontinhos = pontinhos -3
    else:
        pontinhos = 0

    if ('...' in texto[200:] != False):
        pontinhos2 = str.count(texto[200:], '...')
        pontinhos2 = pontinhos - 2
    else:
        pontinhos2 = 0

    coisinhas = ponto+ex+inter+pontinhos+pontinhos2
    lista_range = list(range(coisinhas))

    return len(lista_range)