def conta_frases(texto):
    """função que conta as frases numa string separadas por ponto final, de exclamção interrogação ou reticencias
    str->int"""
    textoalt= str.replace(texto,'...', '/')
    return str.count(textoalt,'.')+return str.count(textoalt,'/')+return str.count(textoalt,'?')return str.count(textoalt,'!')