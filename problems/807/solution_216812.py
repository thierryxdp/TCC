def conta_frases(texto):
    """Retorna o número de frases que aparecem em texto.
    str->int"""
    return str.count((texto),'.')+str.count((texto),'!')+str.count((texto),'?')+(str.count((texto),'...')-3.str.count((texto),'...'))