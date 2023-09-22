def conta_frases(texto):
    '''conta o número de frases em um texto'''
    return str.count(texto,'. ')+str.count(texto,'...')+str.count(texto,'.'')+str.count(texto,'!')+str.count(texto,'?')