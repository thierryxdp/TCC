def conta_frases(texto):
    '''Função que dado um texto em uma string, retorna a quantidade de frases desse texto
    str -> int'''
    
    a = str.count(texto,'.')
    b = str.count(texto,'!')
    c = str.count(texto,'?')
    d = str.count(texto,'...')
    
    if d != 0:
        return a + b + c + d - (d*3)
    
    else:
        return a + b + c + d