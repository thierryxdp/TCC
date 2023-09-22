def uppCons(frase):
    s = ''
    for letraCons in frase:
        if letraCons in 'BCÇDFGHJKLMNPQRSTVXWYZbcçdfghjklmnpqrstvxwyz':
            s += letraCons.upper() 
        else: 
            s += letraCons
    return s