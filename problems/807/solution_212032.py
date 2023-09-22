def conta_frases(frase):
    """conta o numero de frases no texto
    str->int"""
    s=str.split(frase,'!') and
    str.split(frase,'.') and 
    str.split(frase,'?')and 
    str.split(frase,'...')
    t=len(s)
    return  t