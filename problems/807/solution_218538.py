def conta_frases(frase):
    """Conta a quantidade de frases em um texto;
    str -> int"""
    return len(str.split(frase,'.','!','?','...')