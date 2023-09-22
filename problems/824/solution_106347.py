def uppCons(frase):
    i=0
    consoantes=''
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxy":
            consoante = consoante + frase[i]
        i=i+1
	return consoante