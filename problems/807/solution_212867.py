def conta_frases(texto):
    subs = str.replace(str.replace(str.replace(texto,"?","."),"!","."),"...",".")
    return len(subs.split("."))