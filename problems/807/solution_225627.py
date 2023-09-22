def conta_frases(texto):
    '''Função que conta a quantidade de frases que aparecem
    no texto de entrada
    '''
    frases=texto(0)
    frases=frases.split('.')
    frases=frases.split('...')
    frases=frases.split('?')
    frases=frases.split('!')
    
    return len(frases)