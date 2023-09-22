def uppCons (frase):
    frase_nova = list() 
    i = 0
    while (i < len(frase)):
        if(frase[i] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'):
            list.append(frase_nova, str.upper(frase[i]))
            
        else:
            list.append(frase_nova, frase[i])
        
        i += 1
	return str.join('', frase_nova)