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
    frase.lower(frase)
        
    return frase