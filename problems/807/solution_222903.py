def conta_frases(texto):
    """dado um texto, a função retorna o número de frases desse texto;
    str->int"""
    texto=str.replace(texto,'!','.')
    texto=str.replace(texto,'...','.')
    texto=str.replace(texto,'?','.')
    texto=str.split(texto,'.')
    return len(texto)-1