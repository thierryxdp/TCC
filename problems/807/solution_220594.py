def conta_frases(texto):
    '''ao inserir um texto (entre aspas), retorna
    o número de frases contidas no texto.
    str -> int'''
    texto = texto.replace('?', '.')
    texto = texto.replace('!', '.')
    texto = texto.split('. ')
    return texto