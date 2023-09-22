def uppCons(frase):
    i=0
    vogais='aeiou'
    while i<len(frase):
        if frase[i] not in vogais:
            frase=frase.replace(frase[1],frase[i].upper())
        vogais=0
        i=i+1
    return frase