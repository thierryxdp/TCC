def conta_frases (texto):
    if "." in texto:
        texto = texto.split(".")
    if "!" in texto:
        str(texto) = texto.split("!")
    if "?" in texto:
        str(texto) = texto.split("?")
    if "..." in texto:
        str(texto) = texto.split("...")
    return len([texto])