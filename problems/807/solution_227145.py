def conta_frases(texto):
    '''conta o numero de frases em um texto. str->int'''
    return str.count(texto,"!") + str.count(texto,"?") + str.count(texto,".") + str.count(texto,"...") - str.count(texto," ")