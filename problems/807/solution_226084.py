def conta_frases(texto):
    """retorna o número de palavras em uma frase. (str->int)"""
    frases = str.split(texto,".")
    return len(frases)