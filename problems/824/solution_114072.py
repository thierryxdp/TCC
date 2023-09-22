def uppCons (frase):
    i = 0
    f = frase
    while i <len(frase):
        if str(frase[i]) in "aeiouAEIOU":
            frase [i] = frase [i]
        	i = i + 1
        else:
            frase[i] = frase[i].upper()
        	i = i + 1
    return f