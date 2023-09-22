def uppCons(texto): 
    indice=0
    frase='' 
    while indice<len(texto):
        if texto[indice] in 'bcdfghjklmnpqrstvxywzç':
            frase = frase + str.upper(texto[indice])  
    return frase