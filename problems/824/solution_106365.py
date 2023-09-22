def uppCons(frase):
    i=0
    consoante=''
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxyBCDFGHJKLMNPQRSTVWXY":
            
            consoante = consoante + frase[i-1] + frase[i].upper()
            
        i=i+1
	return consoante