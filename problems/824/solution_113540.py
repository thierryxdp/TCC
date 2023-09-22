def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        
        consoante = str.upper(consoante)
        frase!=consoante
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            consoante = consoante+(frase[indice])
            
        indice+=1
    return consoante