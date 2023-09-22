def uppCons(frase):
    '''eae'''
    i=0
    vogais="aeiou"
    while i<len(frase):
        if frase[i] != vogais:
        	frase=frase[i+3].upper()
        if frase[i] == vogais:
            frase=vogais
        i=i+1
    return frase