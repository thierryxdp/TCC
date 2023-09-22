def uppCons(frase):
    '''...'''
   
    consoante = 'S'
    indice = 0
    
    while indice<len(frase): 
        
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            consoante = consoante+str.upper(frase[indice])
            
        indice+=1
    return consoante