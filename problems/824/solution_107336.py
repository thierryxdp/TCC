def uppCons(f):
    '''Recebe uma frase e retorna essa frase com todas as suas consoantes maiúsculas.
str -> str'''
    x = 0
    f_1 = ''
    while x < len(f):
        if (f[x]) not in 'aeiou':
            f_1 = f_1 + f[x].upper()
        else:
            f_1 = f_1 + f[x].lower()
        x = x + 1
    return f_1