def substitui(s, x, i):
    '''função que tem três entradas, repectivamente str, caractere e um número int, e retorna uma string que substitui o caractere de número i na string original pelo caractere x'''
    return s[0:i-1] + str(x) + s[i:]