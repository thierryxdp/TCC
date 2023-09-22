def uppCons(frase):
    '''recebe uma frase e a retorna com consoantes em letra maiuscula
    str->str'''
    frase1=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase[i]=str.upper(frase[i])
        i=i+1
        frase1=frase1+frase[i]
    return frase1