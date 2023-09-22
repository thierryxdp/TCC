def uppCons(frase):
    '''recebe uma frase str e retorna a frase com as
consoantes em maiúscula'''
    indice=0
    frasefinal=''
    letra=''
    while indice<len(frase):
        letra=frase[indice]
        if letra in 'bcdfghjklmnpqrstvwxyzç':           
            frasefinal=frasefinal+letra.upper()
        else:
            frasefinal=frasefinal+letra
        indice+=1
    return frasefinal