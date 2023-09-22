def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            consoante = str.upper(consoante)+(frase[indice])
            
        indice+=1
    return consoante