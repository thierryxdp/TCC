def uppCons(frase):
    frase1 = ""
    for letter in frase:
        if letter not in "ãóéáúíôâaeiouAEIOU":
            frase1 = frase1 + letter.upper()
        else:
            frase1 = frase1 + letter.lower()
    return frase1