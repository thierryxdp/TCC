def conta_frases(x):
    """A função conta o numero de frases contidas na entrada, um texto.str->int"""
    s=str.count(x, " ")
    a=str.count(x,"!")
    b=str.replace(x,"..."," ")
    b2=str.count(b," ")
    c=str.count(x,"?")
    d=str.count(b,".")
    return a+(b2-s)+c+d