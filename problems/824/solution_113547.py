def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        consoante = str.upper(consoante)
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            consoante = str.lower(frase)
            
        indice+=1
    return consoante