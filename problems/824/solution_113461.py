def uppCons(frase):
    '''...'''
   
    consoante= ''
    indice = 0
    
    while indice<len(frase):
        if frase[indice] not in 'aeiouáéíóúã':
            consoante= str.upper(frase)
        indice+=1
    return consoante