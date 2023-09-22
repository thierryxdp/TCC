def conta_frases(texto):
    '''Recebe um texto e retorna o número de frases no mesmo.
    string -> int'''

    s = texto
    a = str.count(texto,'!')
    b = str.count(texto,'?')
    c = str.count(texto,'.')
    d = str.count(texto,'...')
    
    return a + b + c + d - (d*3)