def uppCons (frase):
    frase.upper()
    frase = list(frase)
    for i in range(len(frase) -1):
        if frase[i] in "aeiou":
            frase[i] = frase[i].lower()
    frase = "".join(frase)
    return frase