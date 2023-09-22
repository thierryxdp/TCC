def uppCons(texto):  
    indice=0
    frase=''
    while indice<len(texto):
        if texto[indice] in 'bcdfghjklmnpqrstvxywz':
            frase = frase + str.upper(texto[indice])  
        else:
            frase = frase + texto[indice]
        i=i+1
    return frase