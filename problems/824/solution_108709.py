def uppCons(frase):
    cont = 0
    palavra = ' '
    while cont < len(frase):
        if frase[cont] in 'bcdfghjklmnpqrstvwxz':
            k = str.upper(frase[cont])
            palavra = palavra + k
            cont += 1
		else:
            palavra = palavra + frase[count]
            cont += 1
 	return palavra