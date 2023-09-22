def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            consoante = consoante+1
            
        indice+=1
        
    return consoante