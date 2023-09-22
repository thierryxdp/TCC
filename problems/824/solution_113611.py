def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            consoante = str.upper(frase[indice])+frase
            
        indice+=1
    return consoante