def uppCons(frase):
    '''...'''
    vogal = str.lower(frase)
    consoante = str.upper(vogal)
    indice = 0
    
    while indice<len(frase):
        if frase[indice] not in 'aeiouáéíóúã':
            consoante+=vogal[indice]
        indice+=1
    return consoante