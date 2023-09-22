def uppCons(frase):
    consoantes='bcdfghjklmnpqrstvxwyz'
    proximo=0
    while proximo!=len(frase):
        if frase[proximo] in consoantes:
            novafrase=str.replace(frase,frase[proximo],str.upper(frase[proximo]))
        novafrase=str.replace(frase,frase[proximo],str.upper(frase[proximo]))
        proximo=proximo+1
    return novafrase