def conta_frases(texto):
    '''Função que dado um texto em uma string, retorna a quantidade de frases desse texto
    str -> int'''
    
    a = str.count(texto,'.')
    b = str.count(texto,'!')
    c = str.count(texto,'?')
    d = str.count(texto,'...')
    
    return a + b + c + d