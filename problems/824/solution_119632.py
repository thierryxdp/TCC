def uppCons(frase):
    '''Essa função retorna uam frase cuja as consoantes estão na forma maiúscula,
    str->str'''
    letra=0
    while letra<len(frase):
        if frase[letra] in 'bcdfghjklmnpqrstvwxyz':
           consoante=str.upper(frase[letra])
        letra+=1
    return consoante