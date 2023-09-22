def uppCons(frase):
    '''...'''
    consoante != 'a'
    consoante = str.upper(frase)
    indice = 0
    
    while indice<len(frase):
        if frase[indice] not in 'aeiouáéíóúã':
            consoante+=frase[indice]
        indice+=1
    return consoante