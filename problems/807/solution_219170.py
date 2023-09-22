def conta_frases(frases):
    """Conta o número de frases contidas na entrada;
    str -> int"""
    frase1= str(frases.split("..."))
    frase2= str(frase1.split("!"))
    frase3= str(frase2.split("?"))
    frase4= str(frases.split("."))
    frase5= strip(frase4)
    return len(frase5)