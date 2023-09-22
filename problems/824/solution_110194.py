def uppCons(frase):
    '''eae'''
    i=0
    vogais="aeiouAEIOU"
    while i<len(frase):
        if frase[i] != vogais:
        	frase=frase[i].upper()
        i=i+2
    return frase