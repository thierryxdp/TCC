def conta_frases(txt):
    """
    Retorna quantas frases tem um texto (txt), sendo as
    frases delimitadas por . ? ! ou ...
    """
    delm = "{}"
    txt = txt.replace("...", delm)
    txt = txt.replace(".", delm)
    txt = txt.replace("!", delm)
    txt = txt.replace("?", delm)
    return len( txt.split(delm) ) - 1