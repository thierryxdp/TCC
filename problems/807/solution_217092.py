def conta_frases(texto):
    '''função que conta o número de frases em um texto:
    str -> int'''
    valor = texto.count("!") + texto.count("?") + texto.count("...") + texto.count('.')
    ret = texto.count("...")*3
    return valor - ret