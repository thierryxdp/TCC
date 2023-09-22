def conta_frases (texto):
    texto = str.replace(texto, "...","#")
    texto = str.replace(texto, ".","#")
    texto = str.replace(texto, "!","#")
    texto = str.replace(texto, "?","#")
    return len (str.split(texto,"#")) - 1