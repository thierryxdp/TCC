def uppCons (frase):
    """
    """
    frase1 = frase
    for letra in frase:
        if letra not in "aeiou":
            frase1 = frase1.replace(frase1,frase.upper())
            return frase1