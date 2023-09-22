def conta_frases(texto):
    """conta um numero de frases presentes num texto
    str->int"""
    frases=str.replace(texto,'!','.')
    frases=str.replace(texto,'?','.')
    frases=str.replace(texto,'...','.')
    frases=str.split(texto,'.')
    return len(frases)