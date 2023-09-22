def uppCons (frase):
    i=0
    consoante=''
    consoanteMin='bcdfgjklmnpqrstvwxz'
    CONSOANTE=consoanteMin.upper()
    while i<len(frase):
        if frase[i] in 'bcdfgjklmnpqrstvwxz':
			frase=frase.replace(consoanteMin,CONSOANTE)
        i=i+1
   	return frase