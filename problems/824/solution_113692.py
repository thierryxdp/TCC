def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        caractere = frase[indice]
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyz':
            str.upper(caractere[indice])
            consoante = consoante+caractere
        str.upper(consoante) 
        indice+=1
    return consoante