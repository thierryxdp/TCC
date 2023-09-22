def uppCons (frase):
    """
    """
    frase1 = frase
    for letra in frase:
        if letra not in "aeiou":
            frase1 = frase1.replace(i,frase1.upper())
            return frase1