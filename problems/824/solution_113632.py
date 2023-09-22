def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        str.upper(frase[indice])   
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            consoante = consoante
            
        indice+=1
        
    return consoante