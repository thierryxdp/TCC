def uppCons(frase):
    '''eae'''
    i=0
    vogais="aeiouAEIOU"
    while i+2<len(frase):
        if frase[i] != vogais:
        	frase=frase[i].upper()
        i=i+1
    return frase