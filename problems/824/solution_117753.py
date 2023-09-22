def uppCons(frase):
    '''função que retorne a frase com as consoantes em letras maiusculas da uma frase anterior com todas as letras em minusculo
    str->str'''
    proximo = 0
    palavras = ' '
    while proximo<len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstvwxyz':
            palvaras= palavras + str.upper(frase[proximo])
        proximo = proximo + 1
    return palavras