def conta_frases(x):
    """A função conta o numero de frases contidas na entrada, um texto.str->int"""
    a=str.count(x,"!")
    b=str.replace(x,"...","*")
    b2=str.count(b,"*")
    c=str.count(x,"?")
    d=str.count(b,".")
    return a+b2+c+d