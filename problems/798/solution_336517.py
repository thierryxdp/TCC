def freq_palavras(frases):
    '''A função conta a ocorrência das palavras e retorna em formato de
    dicionários
    
    str -> dicionário'''
    
    i = 0
    y = {}
    a = str.split(frases)
    
    while len(a) > i:
        if a[i] not in y:
            y[a[i]] = (str.count(a, a[i]))
        i = i + 1
        
    return y