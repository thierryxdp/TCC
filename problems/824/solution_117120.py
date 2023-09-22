def uppCons(frase):
    nova_frase=''
    i=0
    while i < len(frase):
        letra = frase[i]
        if letra.lower() in 'bcdfghjklmnpqrstvwxyzç':
        	letra = str.upper(letra)
		nova_frase+= letra
		i+=1
	return nova_frase