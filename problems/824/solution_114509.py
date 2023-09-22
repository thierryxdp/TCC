def uppCons(frase):
    '''recebe uma frase e retorna ela com todas suas
    consoantes em maiúscula
    str->str'''
    cont=0
    acum=''
    while cont<len(frase):
        if frase[cont]in'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            acum=acum+str.upper(frase[cont])
        else:
            acum=acum+frase[cont]
        cont=cont+1
    return acum