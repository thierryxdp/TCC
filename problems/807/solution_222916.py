def conta_frases(frase):
    """função que retorna a quantidade de frases num texto
    str -> int"""
    if '...' in frase:
        return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'...')
    else:
        return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'.')