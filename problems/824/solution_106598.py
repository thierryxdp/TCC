def uppCons(frase):
    """ a função recebe uma frase e a retorna com as vogais maiusculas
    e as consoantes minusculas;
    str->str"""
    i2=0
    conso = ''
    f = [frase]
    while i2<len(f):
        if f[i2] in 'bcdfghjklmnpqrstvwxyz':
            conso = conso + f[i2]
        i2=i2+1
        CONSO = conso.upper()
    return f.replace(conso,CONSO)