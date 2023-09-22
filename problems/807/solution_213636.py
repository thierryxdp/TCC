def conta_frases(frase):
    """Informa quantas frases há no texto dado
    string->int"""
    g=str.replace(frase,"!",".")
    h=str.replace(g,"?",".")
    i=str.replace(h,"...",".")
    i=str.strip(i,'.')
    return len(str.split(i,'.'))