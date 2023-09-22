def uppCons(texto):
    indice=0
    frase=''

    while indice<len(texto):
        if texto[indice] not in 'AEIOUaeiouáéíóúÁÉÍÓÚÂâÃã':
            frase=frase+str.upper(texto[indice])

        else:
            frase=frase+texto[indice]
            
        indice=indice+1

    return frase