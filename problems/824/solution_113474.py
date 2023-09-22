def uppCons(frase):
    '''...'''
   
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        if frase[indice] in str.upper('bcdfghjklmnpqrstvwxyz'):
            consoante = str.upper(frase)
        indice+=1
    return consoante