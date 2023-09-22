def conta_frases (texto):
    '''
    ('.', '!','...','?')
    '''
    ponto =str ('.', '!','...','?')
    return len(str.split(texto, (ponto)))