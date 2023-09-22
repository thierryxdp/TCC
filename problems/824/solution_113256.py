def uppCons(frase):
    '''...'''
    
    vogal = ''
    indice = 0
    
    while indice<len(frase):
        if frase[indice] in 'aeiouáéíóúã':
            vogal+=str.lower(frase[indice])
            indice+=1
            return frase