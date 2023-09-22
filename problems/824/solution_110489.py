def uppCons (frase):
    '''Função, dada uma frase, retorna as consoantes em letra
    maiuscula str -> str'''

    frase_nova = list() 
    i = 0
    while (i < len(frase)):
        if(frase[i] in 'bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZç'):
            list.append(frase_nova, str.upper(frase[i]))
            
        else:
            list.append(frase_nova, frase[i])
        
        i += 1
	return str.join('', frase_nova)