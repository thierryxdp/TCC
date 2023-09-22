def conta_frases(texto):
    """ str -> int;
    Função que conta o número de frases que aparecem no texto."""
    r = texto.split('. ')
    '. ' = '...' and '!' and '?'
    return len(r)