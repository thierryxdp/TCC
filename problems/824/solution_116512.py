def uppCons(frase):
    '''Dada uma frase qualquer, a função retorna a frase
    com todas as suas consoantes em maiúsculo.
    str -> str'''
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyzç':
            s += caractere.upper()
    return s