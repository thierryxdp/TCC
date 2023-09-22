def conta_frases(texto):
    '''retorna o num de frases escritas no texto do arg
    pode estar separada por ! , ? , . ou ...
    str -> int'''
    
    a = str.count(texto , '.')
    b = str.count(texto , '...')
    c = str.count(texto , '!')
    d = str.count(texto , '?')

    if a != 0 and b != 0:
        return (a - 3*b) + c + d + b
    else:
        return a + b + c + d