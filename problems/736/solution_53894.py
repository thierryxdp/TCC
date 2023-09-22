def concatenacao(a, b):
    '''Concatena duas strings a, b na forma abba.
       str, str -> str'''
    return a+b+(a+b)[::-1]