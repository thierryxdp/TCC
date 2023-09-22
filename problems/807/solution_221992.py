def conta_frases(texto):
    """conta um numero de frases presentes num texto
    str->int"""
    texto=str.replace(texto,'!','.')
    texto=str.replace(texto,'?','.')
    texto=str.replace(texto,'...','.')
    texto=str.rtrip(texto,'.')
    frases=str.split(texto,'.')
    return len(frases)