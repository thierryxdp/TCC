def conta_frases(texto):
    '''dado um texto de entrada a função conta o número de frases que aparecem neste texto'''
    return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'...') + str.count(.)