def uppCons(frase):
    consoantes='bcdfghjklmnpqrstvxwyz'
    proximo=0
    novafrase=''
    while frase[proximo]!=len(frase)-1:
        if frase[proximo] in consoantes:
        	novafrase=novafrase+str.upper(frase[proximo])
        else:
            novafrase=novafrase+frase[proximo]
        proximo=proximo+1
    return novafrase