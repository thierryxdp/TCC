def freq_palavras(frases):
    '''A função conta a ocorrência das palavras e retorna em formato de
    dicionários
    
    str -> dicionário'''
    
    x = ''
    i = 0
    y = {}
    
    while len(frases) > i:
        if frases[i] not in x:
            x = x +