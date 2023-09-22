def uppCons(frase):
    '''Retorna a frase dada, com as
    suas consoantes em maiúsculo
    str --> str'''
    frase_maiusculo = ''
    i=0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ':
            frase_maiusculo += str.upper(frase[i])
        else:
            frase_maiusculo += frase[i]
        i+=1
    return frase_maiusculo