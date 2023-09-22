def conta_frases(txt):
    """
    Retorna quantas frases tem um texto (txt), sendo as
    frases delimitadas por . ? ! ou ...
    """
    delm = {}
    txt.replace("...", delm)
    txt.replace(".", delm)
    txt.replace("!", delm)
    txt.replace("?", delm)
    return len( txt.split(delm) )