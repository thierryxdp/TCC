def conta_frases(texto):
    """Essa função conta o número de frases no texto. Considera-se
    o final de uma frase os símbolos:("!",".","?","..."). str->int"""
    frase = str.find(',')
    return len(frase)