def uppCons (frase):
    """
    """
    frase1 = frase
    for letra in frase:
        if letra not in ("a","e","i","o","u"):
            frase1 = frase1.replace(letra,frase1.upper())
        return frase1