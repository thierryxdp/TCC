def uppCons(texto):
    indice=0
    frase_nova=''
    while indice<len(texto):
        if texto[indice] in 'bcdfghjklmnpqrstvxz':
            frase_nova += str.upper(texto[indice])
        if texto[indice] not in 'bcdfghjklmnpqrstvxz':
            frase_nova+=texto[indice]
        indice=indice+1
    return frase_nova