def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase): 
        
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase[indice])
            consoante = consoante+frase
            
        indice+=1
    str.upper(consoante)
    return consoante