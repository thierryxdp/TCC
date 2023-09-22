def conta_frases(texto):
    '''Recebe um texto e retorna a quantidade de frases nele
       str -> int
    '''
    texto = texto.replace('...', '.')
    texto = texto.replace('!', '.')
    texto = texto.replace('?', '.')
    return texto.split('.'))