def conta_frase (texto):
    texto = str.replace(texto, "...","#")
    texto = str.replace(texto, ".","#")
    texto = str.replace(texto, "!","#")
    texto = str.replace(texto, "?","#")
    return len (str.split(texto,"#")) - 1