def conta_frases(texto):
    '''Dado um texto armazenado em uma string, retorna o número de frases que aparecem
    neste texto.
    str -> int'''
    
    return str.count(texto,'.','!','?','...')