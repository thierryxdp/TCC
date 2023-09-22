def uppCons(frase):
    '''Essa função retorna uma frase cuja as consoantes estão na forma maiúscula,
    str->str'''
    letra=0
    consoante=''
    while letra<len(frase):
        if frase[letra] in 'bcdfghjklmnpqrstvxwyzç':
           consoante+=str.upper(frase[letra])
        else:
             consoante+=frase[letra]
        letra+=1
    return consoante