def inverte(frase):
    if ":" in frase:
        frase = frase.replace(":", " ")
    if ";" in frase:
        frase = frase.replace(";", " ")
    if "." in frase:
        frase = frase.replace(".", " ")
    if "!" in frase:
        frase = frase.replace("!", " ")
    if "-" in frase:
        frase = frase.replace("-", " ")
    if "," in frase:
        frase = frase.replace(",", " ")
    if "?" in frase:
        frase = frase.replace("?", " ")

    str.lower(frase)
    
    return frase