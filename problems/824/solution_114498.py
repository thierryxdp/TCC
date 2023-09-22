def uppCons(frase):
    '''a funcao recebe uma frase e retorna a frase orifinal com as consoantes em maiusculo;
    str->str'''
    frase1=''
    x=0
    while x<len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvwxyz'':
            frase1=frase1+str.upper(frase[x])
        else:
            frase1=frase1+frase[x]
        x=x+1
    return frase1