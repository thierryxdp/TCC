def uppCons(frase):
    frase1 = frase.upper()
    frase1 = list(frase)
    for i in range(len(frase)):
        if frase[i] in "aeiou":
            frase[i] = frase[i].lower()
    frase1 = "".join(frase)
    return frase1