def uppCons(frase):
    frase1 = frase.upper()
	frase1 = list(frase)
    for i in range(len(frase1)):
        if frase1[i] in "aeiouãúéóí":
            frase1[i] = frase1[i].lower()
    frase1 = "".join(frase1)
    return frase1