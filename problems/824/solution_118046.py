def uppCons(frase):
    s = ''
    for letraCons in frase:
        if letraCons in 'BCDFGHJKLMNPQRSTVXWYZbcdfghjklmnpqrstvxwyz':
            s += letraCons.upper() 
        else: 
            s += letraCons
    return s