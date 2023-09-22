def uppCons(frase):
    """
    """
    nova_frase = frase
    for i in frase:
        if frase[i] not in "aeiou":
            nova_frase = nova_frase.replace(frase[i], nova_frase.upper())
        return nova_frase