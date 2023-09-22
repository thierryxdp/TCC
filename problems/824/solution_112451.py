def uppCons(frase):
    '''kjhgk'''
    nova_frase=''
    indice_frase=0
    string_cons= 'bcçdfghjklmnpqrstvxywz'
    while indice_frase<len(frase):
        if frase[indice_frase] in string_cons:
            nova_frase= nova_frase+str.upper(frase[indice_frase])
            indice_frase= indice_frase+1
        else:
            nova_frase=nova_frase+frase[indice_frase]
            indice_frase= indice_frase+1
    return nova_frase