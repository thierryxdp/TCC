def concatenacao(a, b):
    ''' usar as duas strings a e b e retornar a concatenacao delas como abba;
    str,str -> tup'''
    
    return (a+b) + (a+b[::-1])