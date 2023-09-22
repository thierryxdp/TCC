def uppCons(frase):
    '''eae'''
    i=0
    while i+1<len(frase):
        if frase[i] != "aeiouAEIOU":
        	frase=frase[i].upper()
        i+1
    return frase