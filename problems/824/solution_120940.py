def uppCons(frase):
    '''A funcao recebe uma frase e retorna a mesma frase com apenas as consoantes em
maisculo str->str'''
    ordem=0
    nfrase=''
    while ordem<len(frase):
        if frase[ordem] in 'aeiou ' or 'AEIOU ' == True:
           nfrase+=frase[ordem]
        else:
            nfrase+=frase[ordem].upper()
        ordem=ordem+1
    return nfrase