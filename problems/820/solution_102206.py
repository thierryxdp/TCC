def uppCons(frase):
    '''Dada uma frase, retorna a frase com suas consoantes maiúsculas
str -> str'''
    cons = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    final = ' '
    for caract in frase:
        if caract in cons:
            final += caract.upper()
        else:
            final += caract.lower()
    return final