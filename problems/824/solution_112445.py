def uppCons(frase):
    '''kjhgk'''
    indice_frase=0
    string_cons= 'bcdfghjklmnpqrstvxywz'
    while indice_frase<len(frase):
        if frase[indice_frase] in string_cons:
            frase_alterada= str.upper(frase[indice_frase])
            indice_frase= indice_frase+1
        else:
            frase_alterada= frase_alterada
            indice_frase= indice_frase+1
    return frase_alterada