def uppCons(frase):
    '''---'''
    
    indice = 0
    transformar = ''
    
    
	while indice < len(frase):
        if frase[indice] in 'bcçdfghjklmnpqrstvxwyz':
            transformar += str.upper(frase[indice])
        else:
            transformar += frase[indice]
        indice += 1 
        
    return transformar