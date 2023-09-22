def conta_frases(texto):
    '''retorna o numero de frases no texto'''
    return len(str.count(texto,'!'))