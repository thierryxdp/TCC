def conta_frases(frase):
    """função que retorna a quantidade de frases num texto
    str -> int"""
    frase1 = str.replace(frase,'...','.')
    frase2 = str.replace(frase,'!','.')
    frase3 = str.replace(frase,'?','.')
    return str.count(frase,'.') + str.count(frase1,'.') + str.count(frase2,'.') + str.count(frase3,'.')