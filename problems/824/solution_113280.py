def uppCons(frase):
    '''...'''
    
    consoante = ''
    indice = 0
    
    while indice<len(frase):
        if frase[indice] in 'aeiouáéíóúã':
            consoante+=frase[indice]
        indice+=1
    return consoante