def conta_frases(texto):
    """"""
    texto = str.join("!",str.split(texto, "."))
    texto = str.join("?",str.split(texto,"!"))
    texto = str.join("...",str.split(texto,"?"))
    texto = str.split(texto,"...")
    return len(texto)