def conta_frases(frase):
    """retorna o numero de palavras da frase"""
    frase = str.replace(frase,'!','.')
    frase = str.replace(frase,'?','.')
    frase = str.replace(frase,'...','.')
    frase = str.split(frase,'.')
    return len(frase)-1