def conta_frases(texto):
    """Função que recebe um texto e retorna o número de frases que o compõem."""
    """str-->str"""
    a = str.replace(texto, '...','.')
    b = str.replace(a, '!','.')
    c = str.replace(b, '?','.')

    return len(str.split(c,'.'))