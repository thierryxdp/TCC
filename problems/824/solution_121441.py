q= len(frase)
novafrase=''
i=0
	while i<q:
   		if frase[i] in 'bcçdfghjklmnpqrstwxz':
        	novafrase=novafrase+str.upper(frase[i])
    	else:
        	novafrase=novafrase+frase[i]
    	i=i+1
	return novafrase