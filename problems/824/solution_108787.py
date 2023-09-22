def uppCons (frase):
    f= 0
    novafrase = ""
    vogais= "AEIOUÚÓÃÉúóíÃéaeiou"
    while f < len(frase):
        if frase[f] in vogais:
            novafrase += frase[f]
            f= f+1
        else:
            novafrase += str.upper(frase[f])
            f= f+1
    return novafrase