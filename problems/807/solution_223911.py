def conta_frases(frase):
    """ função que retorna a quantidade de frases num texto
    str -> int"""
    frase1 = str.replace(frase,'!','.')
    frase1 = str.replace(frase1,'...','.')
    frase1 = str.replace(frase1,'.','.')
    frase1 = str.replace(frase1,'?','.')
    x = str.split(frase1,'.')
    return len(x)