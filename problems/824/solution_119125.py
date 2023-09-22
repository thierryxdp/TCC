def uppCons(frase):
    """
    """
    nova_frase = frase
    for letra in frase:
        if letra not in "aeiou":
            nova_frase = nova_frase.replace(letra, nova_frase.upper())
        return nova_frase