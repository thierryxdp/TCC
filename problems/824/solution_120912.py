def uppCons(frase):
    frase1 = frase.upper()
	frase1 = list(frase1)
    for i in range(0,len(frase1)):
        if frase1[i] in "AEIOUÃÍÓÚ":
            frase1[i] = frase1[i].lower()
    frase2 = "".join(frase1)
    return frase2