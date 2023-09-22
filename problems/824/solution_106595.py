def uppCons(frase):
    """ a função recebe uma frase e a retorna com as vogais maiusculas
    e as consoantes minusculas;
    str->str"""
    i2=0
    conso = ''
    while i2<len(frase):
        if frase[i2] in 'bcdfghjklmnpqrstvwxyz':
            conso = conso + frase[i2]
        i2=i2+1
    return conso