def uppCons(texto):
    indice=0
    while indice<len(texto):
        if texto[indice] in 'bcdfghjklmnpqrstvxz':
            str.upper(texto[indice])
        indice=indice+1
    return texto