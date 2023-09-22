def uppCons(frase):
    i=0
    vogais='AEIOUaeiou'
    while i<len(frase):
        if frase[i] not in vogais:
            frase.replace(frase[i],frase[i].upper())
        i=i+1
        return frase