def uppCons(frase):
    frase = str.upper(frase)
    frase = list(frase)
    for i in range(len(frase)):
        if frase[i] == "A":
            frase[i] ="a"
        if frase[i] == "E":
            frase[i] = "e"
        if frase[i] == "I":
            frase[i] ="i"
        if frase[i] == "O":
            frase[i] ="o"
        if frase[i] == "U":
            frase[i] ="u"
    frase = "".join(frase)
    return frase