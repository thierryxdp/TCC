def uppCons(frase):
    '''eae'''
    i=0
    vogais="aeiou"
    while len(frase)>i:
        if frase[i] != vogais:
        	frase=frase[i].upper()
            i=i+1
   
    return frase