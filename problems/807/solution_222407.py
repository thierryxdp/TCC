def conta_frases(texto):
    """A função recebe um texto e devolve o numero de frases que o texto possui. Uma oração só é contada
    como frase se terminar em um desses caracteres: Ponto final, Interrogação, Exclamação ou reticencias;
    str -> int"""
    str.replace(texto, '!', '.')
    str.replace(texto, '?', '.')
    str.replace(texto,'...','.')
    lista1 = str.split(texto, '.')
    return len(lista1)