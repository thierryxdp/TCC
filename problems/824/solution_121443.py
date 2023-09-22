def uppCons(frase,novafrase):    
Q= len(frase)
novafrase=''
i=0
	while i < Q:
   		if frase[i] in 'bcçdfghjklmnpqrstwxz':
        	novafrase=novafrase+str.upper(frase[i])
    	else:
        	novafrase=novafrase+frase[i]
    	i=i+1
	return novafrase