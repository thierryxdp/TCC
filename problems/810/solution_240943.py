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

    fraselist = frase.split(" ")
    
    return frase