def conta_frases(frase):
    """Conta a quantidade de frases em um texto;
    str -> int"""
    return str.replace(frase,'!','.') str.replace(frase,'?','.') str.replace(frase,'...','.')len(str.split(frase,'.'))