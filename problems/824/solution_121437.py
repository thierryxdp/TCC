Q= len(frase)
frase=''
i=0

	while i<Q:
   		if f[i] in 'bcçdfghjklmnpqrstwxz':
        	frase=frase+str.upper(f[i])
    	else:
        	frase=frase+f[i]
    	i=i+1
	return frase