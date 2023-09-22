def uppCons(frase):
    '''...'''
    
    c = str.upper(consoante)
    indice = 0
    
    while indice<len(frase):
        if frase[indice] not in 'aeiouáéíóúã':
            c+=frase[indice]
        indice+=1
    return c