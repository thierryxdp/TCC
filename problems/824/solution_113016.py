def uppCons (frase):
    i=0
    frase=''
    while i < len(frase):
      	if frase[i] in 'bcdfgjklmnpqrstvwxz':
            low='bcdfgjklmnpqrstvwxz'
            	c=(frase[i]).upper()
    			frase=frase.replace(low,c)
        i=i+1
    	return frase