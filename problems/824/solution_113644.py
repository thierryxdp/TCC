def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase): 
        
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            consoante = consoante+(frase[indice.upper])
            
        indice+=1
   
    return consoante