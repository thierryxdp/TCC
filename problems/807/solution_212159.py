def conta_frases(texto):
    """ Retorna o número de frases que um texto possui;
    str->int"""
    t=str(texto)
    return len(str.split(t,'.'or'!'or'?'or'...')