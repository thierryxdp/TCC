def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase): 
        caractere = str.upper(frase[indice])
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            consoante = consoante+caractere
      
        indice+=1
    return consoante