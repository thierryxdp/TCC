def conta_frases(frase):
    """retorna o numero de pontos finais na frase"""
    frase = str.replace(frase,'!','.')
    frase = str.replace(frase,'?','.')
    frase = str.replace(frase,'...','.')
    frase = str.split(frase,'.')
    return len(frase)