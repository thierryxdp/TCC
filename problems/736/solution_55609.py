def concatenacao(a, b):
    '''Função que dado duas strings a e b, retorna a concatenação delas no formato abba;
       str, str -> str'''
    x=(a,b)
    return x[0], x[1], x[-1], x[-2]