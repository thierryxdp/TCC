def conta_frases(texto):
    ''' conta o número de frases no texto
    string -> int'''
    fimdefrase = '.','!','?','...'
    return str.count(texto,fimdefrase)