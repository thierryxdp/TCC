def uppCons(frase):
    consoantes='bcdfghjklmnpqrstvxwyz'
    proximo=0
    while frase[proximo]!=len(frase):
        if frase(proximo) in consoantes:
        	return str.replace(frase,frase[proximo],str.upper(frase[proximo]))
    else:
        return frase