def conta_frases(frase):
    """retorna o numero de pontos finais na frase"""
    frase = str.replace(frase,'!','.')
    frase = str.replace(frase,'?','.')
    frase = str.replace(frase,'...','.')
    return str.count(frase,'.')