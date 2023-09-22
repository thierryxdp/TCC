def conta_frases(texto):
    """conta um numero de frases presentes num texto
    str->int"""
    str.replace(texto,'!','.')
    str.replace(texto,'?','.')
    str.replace(texto,'...','.')
    frases=str.split(texto,'.')
    return len(frases)