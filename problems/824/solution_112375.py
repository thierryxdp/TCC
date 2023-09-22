def uppCons(frase):
    '''recebe uma frase str e retorna a frase com as
consoantes em maiúscula'''
    indice=0
    frasefinal=''
    while indice<len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            frasefinal=frasefinal+frase.upper(frase[indice])
        else:
            frasefinal=frasefinal+frase[indice]
        indice+=1
    return frasefinal