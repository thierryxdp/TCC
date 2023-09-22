def conta_frases(frases):
    """teste"""
    frases = str.replace(frases,"?",".")
    frases = str.replace(frases,"!",".")
    frases = str.replace(frases,"...",".")
    contafrases = str.split(frases,".")
    return int(len(contafrases))