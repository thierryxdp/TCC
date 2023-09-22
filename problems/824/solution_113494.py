def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            consoante = consoante+frase[indice]
        indice+=1
    return str.upper(consoante)