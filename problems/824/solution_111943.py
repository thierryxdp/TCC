def uppCons(frase):
    '''---'''
    
    indice = 0
    transformar = ''
    
    
   	while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvxwyz':
            transformar += str.upper(frase[indice])
        indice += 1 
        
    	   return transformar