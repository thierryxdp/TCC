def uppCons(frase):
    '''dada uma frase, a funcao retorna esta mesma frase com as consoantes em maiusculo
    str -> str'''
    final = ''
    for i in frase:
        if i in 'bcdfghjklmnpqrstvwxyz':
            final += str.upper(i)
        else:
            final += i
    return final