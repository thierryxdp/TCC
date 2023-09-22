def conta_frases(frases):
    ''' Essa função calcula o número de frases contidas em um texto, str,str,int'''
    return str.count(frases,'...') + str.count(frases,'?') + str.count (frases,'!')