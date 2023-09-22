def uppCons(frase):
    i=0
    consoante=''
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxy":
            
            consoante = consoante + frase.upper()
        i=i+1
	return consoante