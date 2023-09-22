def uppCons (frase):
    i=0
    fraseF=''
    while i < len(frase):
      	if frase[i] in 'bcdfgjklmnpqrstvwxz':
            low = 'bcçdfghjklmnpqrstvwxyz
            up = 'BCÇDFGHJKLMNPQRSTVWXYZ'         
    		fraseF= frase.replace(low,up)
        i=i+1
    	return frase.replace(low,up)