def conta_frases(text):
    """
    retorna o número de palavras em um texto
    str -> int
    """
    frases = str.split(text, ('.', '!', '?', '...'))
    return len(frases)