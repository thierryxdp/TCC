def uppCons(frase):
    '''kjhgk'''
    Cons_Maiusculas=frase
    indice_frase=0
    string_cons= 'bcdfghjklmnpqrstvxywz'
    while indice_frase<len(frase):
        if Cons_Maiusculas[indice_frase] in string_cons:
            str.upper(Cons_Maiusculas[indice_frase])
            indice_frase= indice_frase+1
        else:
            indice_frase= indice_frase+1
    return Cons_Maiusculas