def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas as suas consoantes em maiúscula;
       str->str'''
    novafrase = ''
    for letraCons in frase:
        if letraCons in 'BCÇDFGHJKLMNPQRSTVWXYZbcçdfghjklmnpqrstvwxyz':
            novafrase += letraCons.upper()
        else:
            novafrase += letraCons
    return novafrase