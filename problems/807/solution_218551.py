def conta_frases(frase):
    """Conta a quantidade de frases em um texto;
    str -> int"""
    str.replace(frase,'!','.')
    str.replace(frase,'?','.')
    str.replace(frase,'...','.')
    return len(str.split(frase,'.'))