def uppCons(frase):
    frase1 = frase.upper()
	frase1 = list(frase1)
    for i in range(1,len(frase1)):
        if frase[i] in "aeiouãúéóí":
            frase[i] = frase[i].lower()
    frase2 = "".join(frase1)
    return frase2