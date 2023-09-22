def conta_frases(texto):
    "função que conta o numero de frases que aparecem no texto"
    texto = texto.replace("!", ".")
    texto = texto.replace("?", ".")
    texto = texto.replace("...", ".")
    return texto.count(".")