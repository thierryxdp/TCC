def conta_frases(texto):
    '''retorna o numero de frases no texto'''
    return len(texto.split('!')) and len(texto.split('?')) and len(texto.split('.'))