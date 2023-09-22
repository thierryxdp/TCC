def uppCons(frase):
    '''...'''
    
    consoante = str.upper(frase)
    indice = 0
    
    while indice<len(frase):
        if frase[indice]  in 'aeiouáéíóúã':
            consoante=frase[indice]
        indice+=1
    return consoante