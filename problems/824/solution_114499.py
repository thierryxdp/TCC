def uppCons(frase):
    minus= 'bcdfghjklmnpqrstvwxyz'
    maius= 'BCDFGHJKLMNPQRSTVWXYZ'
    frasefinal= str.mketrans(minus,maius)
    return frase.translate(frasefinal)