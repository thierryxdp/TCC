def uppCons (frase):
    frase.upper()
    frase = list(frase)
    for i > 1 in range(len(frase)):
        if frase[i] in "aeiou":
            frase[i] = frase[i].lower()
    frase = "".join(frase)
    return frase