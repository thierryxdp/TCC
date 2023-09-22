def uppCons (frase):
    f=0
    novafrase= " "
    vogais= "AEIOUaeiou"
    while f< len(frase):
        if frase[f] != vogais:
            novafrase += str.upper(frase[f])
            f=f+1
        else:
            novafrase+= frase[f]
            f= f+1
        return novafrase