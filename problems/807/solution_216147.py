def conta frases (texto):
    '''Conta o número de frases encontradas em um texto
    string-> int'''
    n1 = len(str.split(texto,'.'))
    n2 = len(str.split(texto,'!'))
    n3 = len(str.split(texto,'?'))
    n4 = len(str.split(texto,'...'))
    return n1 + n2 + n3 + n4 - 1