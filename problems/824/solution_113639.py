def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase): 
        
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            consoante = consoante+str.upper(frase[indice])
            'aeiou'
            
        indice+=1
        
    return consoante