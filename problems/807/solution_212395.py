def conta_frases(x):
    """funcao que conta o numero de frases que aparecem no texto
    str->int"""
    x=str.replace(x,"...","!")
    return str.count(x," ")+str.count(x,"!")+str.count(x,"?")