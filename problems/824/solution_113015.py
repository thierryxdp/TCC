def uppCons (frase):
    i=0
    frase=''
    while i < len(frase):
      	if frase[i] in 'bcdfgjklmnpqrstvwxz':
            	c=(frase[i]).upper()
    			frase+=c
        i=i+1
    	return frase