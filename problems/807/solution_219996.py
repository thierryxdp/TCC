def conta_frases (texto):
    if "." in texto:
        str(texto) = texto.split(".")
    if "!" in texto:
        str(texto) = texto.split("!")
    if "?" in texto:
        str(texto) = texto.split("?")
    if "..." in texto:
        texto = texto.split("...")
    resultado = len([texto])
    return resultado