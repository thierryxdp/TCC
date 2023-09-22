def uppCons (frase):
    i=0
    frase=''
    cMin='bcdfgjklmnpqrstvwxz'
    cMai=cMin.upper()
    while i < len(frase):
      	if cMin in frase:
    		frase=frase.replace(cMin,cMai)
        i=i+1
    	return frase