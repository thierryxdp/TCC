def uppCons(frase):
    '''eae'''
    i=0
    while i<len(frase):
        if frase[i] != "aeiouAEIOU":
        	frase=frase[i].upper()
        if frase[i] == "aeiouAEIOU":
            frase=frase
        i+1
    return frase