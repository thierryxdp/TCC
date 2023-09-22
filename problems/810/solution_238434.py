def inverte(frase):
    """Dado uma frase, retorna ela ao contrario, sem pontuação e sem letras maiusculas. string>string"""
    frase = frase.replace("!"," ")
    frase = frase.replace("."," ")
    frase = frase.replace(":"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace(","," ")
    frase = frase.replace("-"," ")
    frase = frase.replace(";"," ")
    frase = frase.lower()
    frase = frase.split()
    frase = frase[::-1]
    frase = " ".join(frase)
    return frase