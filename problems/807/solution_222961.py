def conta_frases(frase):
    """Função que dada certo texto(string) que retorna o número de
    frases
    'str' -> int"""
    frase = str.replace(frase,'...','.')
    return (str.count(frase, '.') + str.count(frase, '?') + str.count(frase, '!'))