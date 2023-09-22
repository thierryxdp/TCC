def freq_palavras(frases):
    '''A função conta a ocorrência das palavras e retorna em formato de
    dicionários
    
    str -> dicionário'''
    
    i = 0
    y = {}
    a = frases.split()
    
    while len(a) > i:
        if a[i] not in y:
            b = list.count(a, a[i])
            y[a[i]] = b
        i = i + 1
        
    return y