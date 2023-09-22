def conta_frases(texto):
    '''Esta função calcula a quantidade de frases em um texto.
    str->int'''
    frases = str.split(texto, '.')
    return len(frases)