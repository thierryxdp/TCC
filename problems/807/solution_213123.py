def conta_frases(frases):
    '''
        Função que retorna a quantidade de frases em uma String.
        Str -> Int
    '''
    frases=frases.replace('!', '.')
    frases=frases.replace('?', '.')    
    frases=frases.replace('…', '.')
    return (len(frases.split('. ')))