def concatenacao(a, b):
    '''dado duas strings, retorna a concatenacao da 
    primeira string com a inversa da segunda.
    str,str -> str'''
    return a[::] + b[::] + b[::] + a[::]