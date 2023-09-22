def uppCons(frase,novafrase):    

    Q= len(frase)

    novafrase=''

    i=0
	
    while i < Q:
   		if frase[i] in 'bcçdfghjklmnpqrstwxz':
        	novafrase=novafrase+str.upper(frase[i])
    	elif:
        	novafrase=novafrase+frase[i]
    	i=i+1
	return novafrase