def freq_palavras(f):
    '''
    A função recebe uma str e retorna um dicionário
    onde as chaves são palavras da str e o valor delas seja
    a frequência que a palavra aparace 
    '''
    d = {}
    s = str.split(f)
    for x in s:
        d[x] += 1
    return d