def uppCons(frase):
    '''...'''
    
    vogal = ''
    indice = 0
    
    while indice<len(frase):
        if frase[indice] in 'aeiouáéíóúã':
            vogal+=frase.lower([indice])
            indice+=1
            return frase