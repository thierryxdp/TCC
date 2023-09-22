conta_frases(frase):
    """Retorna a quantidade de frases contidas em uma string que é a entrada;
    str->int"""
    return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')