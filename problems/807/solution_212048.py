def conta_frases(frase):
    """conta o numero de frases no texto
    str->int"""
    frase=frase.replace("...","#")
    frase=frase.replace("!","#")
    frase=frase.replace("?","#")
    frase=frase.replace(".","#")
    s=str.split(frase,"#")
    t=len(s)
    return t