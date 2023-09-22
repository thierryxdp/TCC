def conta_frases(x):
    """A função retorna o numero de frases existentes no texto"""
    y = str.replace(x, '...','*')
    return str.count(y, "!") + str.count(y,".") + str.count(y, "?") + str.count(y,"*")