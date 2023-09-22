def conta_frases(frase):
    """Retorna a quantidade de frases contidas em uma string que é a entrada;
    str->int"""
    frase=str.replace(frase,'...','.')
    return str.count(frase,'.') +str.count(frase,'!')+str.count(frase,'?')