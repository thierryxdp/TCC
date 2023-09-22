def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            consoante = consoante+(frase.upper[indice])
            
        indice+=1
    return consoante