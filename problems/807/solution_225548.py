def conta_frases(texto):
    '''Função que calcula e retorna o número de frases de 
    um texto dado na entrada
    str -> int'''
    texto1 = str.replace(texto,'!','.')
    texto1 = str.replace(texto1,'...','.')
    texto1 = str.replace(texto1,'.','.')
    texto1 = str.replace(texto1,'?','.')
    x = str.split(texto1,'.')
    return len(x) - int(1)