def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        caractere = frase[indice]
        if (frase[indice]) in 'bcdfghjklmnpqrstvwxyzç':
            caractere = str.upper(caractere)
        consoante = consoante+caractere
        
        indice+=1
    return consoante