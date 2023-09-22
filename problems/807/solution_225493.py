def conta_frases(txt):
    txt = txt.replace("...",".")
    txt = txt.replace("!",".")
    txt = txt.replace("?",".")
    num_pontos = txt.count(".")
    return num_pontos