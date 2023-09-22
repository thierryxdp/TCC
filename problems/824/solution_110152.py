def uppCons(frase):
    '''eae'''
    i=0
    vogais="aeiouAEIOU"
    while i<len(frase):
        if frase[i] != vogais[i]:
        	frase=frase[i].upper() 
        if frase[i] == vogais[i]:
            frase=frase
        i=i+1
    return frase