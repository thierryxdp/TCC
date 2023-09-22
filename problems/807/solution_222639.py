def conta_frases(frase):
    """função que retorna a quantidade de frases
    str -> str"""
    frase1 = str.strip(frase,'!')
    frase1 = str.strip(frase,'.')
    return frase1