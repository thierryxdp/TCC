def uppCons(frase):
    '''Esta função recebe um afrase como entrada e
retorna  as consoantes em  maiúscula,str->str'''
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper()
        return s