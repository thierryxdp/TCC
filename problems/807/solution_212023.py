def conta_frases(frase):
    """retorna o numero de frases
    str->float"""
    s=str.split(frase,'?',frase,'.') 
    t=len(s)
    return t