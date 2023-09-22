def conta_frases (texto):
    '''
       Dado um texto a função retorna a quantidade de frases
       que está presente no texto
       str -> int
    '''
    return len(str.partition(texto, ('.' or '!' or '?' or '...')))