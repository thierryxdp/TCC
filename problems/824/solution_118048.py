def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas as suas consoantes em letra maiúscula.
    str -> str'''
    s = ''
    for letraCons in frase:
        if letraCons in 'BCÇDFGHJKLMNPQRSTVXWYZbcçdfghjklmnpqrstvxwyz':
            s += letraCons.upper() 
        else: 
            s += letraCons
    return s