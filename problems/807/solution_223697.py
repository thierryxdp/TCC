def conta_frases(texto):
    '''retorna o numero de frases no texto'''
    return len(texto.split('!')) + len(texto.split('?')) + len(texto.split('...'))