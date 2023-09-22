def conta_frases(texto):
    str.replace(texto,"...",".")
    str.replace(texto,"!",".")
    
    str.replace(texto,"?",".")
    return len(texto.split("."))