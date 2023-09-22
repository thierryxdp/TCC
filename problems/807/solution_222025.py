def conta_frases(text):
    """
    retorna o número de palavras em um texto
    str -> int
    """
    frases = str.split(text, ('.' and '!' and '?' and '...'))
    return len(frases)