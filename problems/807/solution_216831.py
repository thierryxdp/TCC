def conta_frases(texto):
    '''conta o número de frases presente em um texto, de acordo com a
    pontuaçao final presente em cada frase.
    str -> int'''
    
    return str.index(texto, "!" or "?" or ".", 0, len(texto))