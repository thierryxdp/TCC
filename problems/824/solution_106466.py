def uppCons(frase):
    '''recebe uma frase e a retorna com consoantes em letra maiuscula
    str->str'''
    frase1=''
    i=0
    while i<len(frase):
        caractere=frase[i]
        if caractere in 'bcçdfghjklmnpqrstvwxyz':
            caractere=str.upper(caractere)
        i=i+1
        frase1=frase1+caractere
    return frase1