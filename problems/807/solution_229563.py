def conta_frases (texto):
    '''
    ('.', '!','...','?')
    return len(str.split(texto, ponto))
    '''
    pontos = '.', '!','...','?'
    return str.count(texto, pontos)