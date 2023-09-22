def conta_frases(texto):
    """A função recebe um texto e devolve o numero de frases que o texto possui. Uma oração só é contada
    como frase se terminar em um desses caracteres: Ponto final, Interrogação, Exclamação ou reticencias;
    str -> int"""
    a = str.replace(texto, '!', '.')
    b = str.replace(a, '?', '.')
    c = str.replace(b,'...','.')
    lista1 = str.split(c, '.')
    return len(lista1)-1