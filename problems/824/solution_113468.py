def uppCons(frase):
    '''...'''
   
    consoante= 'bcdfghjklmnpqrstvwxyz'
    indice = 0
    
    while indice<len(frase):
        if frase[indice] not in 'aeiouáéíóúã':
            consoante= str.upper(consoante)
        indice+=1
    return consoante