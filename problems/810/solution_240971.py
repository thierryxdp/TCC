def inverte(frase):
    frase.lower
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
        frase = frase.replace(",", "")
    if "?" in frase:
        frase = frase.replace("?", " ")

    fraselist = frase.split(" ")
    fraselist[-1:-(len(frase)+1):-1]
    
    
    
    return frase