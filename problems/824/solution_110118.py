def uppCons(frase):
    '''eae'''
    i=0
    vogais="aeiou"
    while i>len(frase):
        if frase[i] != vogais:
        	frase1=frase[i].upper()
        i=i+1
    return frase1