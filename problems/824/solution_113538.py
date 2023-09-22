def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        frase!=consoante
        consoante = str.upper(consoante)
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            consoante = consoante+(frase[indice])
            
        indice+=1
    return frase