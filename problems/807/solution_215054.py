def conta_frases(texto):
    """ . """
    texto1 = str.count(texto, ' ... ')
    frase = str.replace(texto, ' ... ', '')
    texto1 = texto1 + str.count (frase,'!')
    texto1 = texto1 + str.count (frase, '?')
    texto1 = texto1 + str.count (frase, '.')
    return texto 1