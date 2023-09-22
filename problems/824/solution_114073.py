def uppCons (frase):
    i = 0
    f = frase
    frase = ""
    while i <len(frase):
        if str(frase[i]) in "aeiouAEIOU":
            frase = frase + frase [i]
        	i = i + 1
        else:
            frase[i] = frase[i].upper()
        	i = i + 1
    return f