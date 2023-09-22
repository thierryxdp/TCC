def conta_frases(texto):
    """Testando ainda"""
    str.replace(texto,"!",".")
    str.replace(texto,"?",".")
    str.replace(texto,"?",".")
    str.replace(texto,"...",".")
    separadorponto = str.split(texto,".")
    return int(len(str.split(texto,"."))