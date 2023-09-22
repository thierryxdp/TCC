def conta_frases(frase):
    """retorna o numero de palavras da frase"""
    frase = str.replace(frase,'!','.')
    frase = str.replace(frase,'?','.')
    frase = str.replace(frase,'...','.')
    nfrases = str.split(frase,'.')
    return len(nfrases)