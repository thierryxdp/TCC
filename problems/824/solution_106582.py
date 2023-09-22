def uppCons(frase):
    """ a função recebe uma frase e a retorna com as vogais maiusculas
    e as consoantes minusculas;
    str->str"""
    i=0
    i2=0
    vogais = ''
    conso = ''
    while i<len(frase) and i2<len(frase):
        if frase[i] in 'AEIOUaeiou':
            vogais = vogais + frase[i]
        i=i+1
        if frase[i2] in 'BCDFGHJKLMNPQRSTVWXYZbcddfghjklmnpqrstvwxyz':
            conso = conso + frase[i2]
        i2=i2+1
    return vogais + conso