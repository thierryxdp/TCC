def uppCons(frase):
    '''função que recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúscula; str->str'''
    frase1 = ''
    tam = 0
    consoante = 'cdfghjklmnpqrstvwxyz'
    while tam<len(frase):
        if frase[tam] in consoante:
            frase1 = frase1 + (str.upper(frase[tam]))
        else:
            frase1 = frase1 + frase[tam]
        tam = tam + 1
    return frase1