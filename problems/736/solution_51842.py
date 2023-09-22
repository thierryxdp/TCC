def concatenacao(a, b):
    """ Dados duas strings 'a' e 'b', retorna a concatenacao dessas strings
        no formato 'abba' """
    x = (a,b)
    formato = x[0:] + x[-1::-1]
    return formato