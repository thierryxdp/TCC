def conta_frases(txt):
    """Dado um texto qualquer, retorna o número
    de frases do texto.
    str -> int"""
    txt = str.replace(txt,"...",".")
    txt = str.replace(txt,"?",".")
    txt = str.replace(txt,"!",".")
    fr = txt.split(".")
    return len(fr)