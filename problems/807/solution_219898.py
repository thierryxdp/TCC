def conta_frases(texto):
    texto = texto.split(".")
    texto = texto.split("!")
    texto = texto.split("?")
    texto = texto.split("...")
    numero = len(texto)
    return numero