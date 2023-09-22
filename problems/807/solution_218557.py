def conta_frases(frase):
    """Conta a quantidade de frases em um texto;
    str -> int"""
    a = str.replace(frase,'!','.')
    b = str.replace(a,'?','.')
    c = str.replace(b,'...','.')
    return len(str.split(c, '.'))