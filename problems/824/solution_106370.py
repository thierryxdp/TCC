def uppCons(frase):
    i=0
    consoante=''
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXY":
            
            consoante = consoante + frase[i].upper()
        else:
            consoante = consoante + frase[i]
        i=i+1
	return consoante