def uppCons(frase):
    '''Retorna a frase informada com consoantes em maiúsculo.
    str->str'''
    filtro=''
    contador=0
    while contador<len(frase):
        if str.lower(frase[contador]) in 'bcdfghjklmnpqrstvwxyzç':
            filtro += str.upper(frase[contador])
        else:
            filtro += frase[contador]
        contador += 1
    return filtro