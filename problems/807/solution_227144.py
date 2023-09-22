def conta_frases(texto):
    '''conta o numero de frases em um texto. str->int'''
    return str.count(texto,"!",1,-2) + str.count(texto,"?",1,-2) + str.count(texto,".",1,-2) + str.count(texto,"...",1,-2)