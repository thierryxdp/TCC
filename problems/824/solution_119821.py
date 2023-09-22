def uppCons (frase):
    """
    """
    frase1 = frase
    for letra in frase:
        if letra in "aeiou":
            frase1 = frase1.replace(letra,frase1.upper())
            return frase1