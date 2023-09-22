def conta_frases(texto):
    '''Função que dado um texto em uma string, retorna a quantidade de frases desse texto
    str -> int'''
    
    a = str.count(texto,'. ',0, len(texto)-1)
    b = str.count(texto,'!')
    c = str.count(texto,'?')
    d = str.count(texto,'...')
    e = str.count(texto,'.', len(texto)-1,len(texto))
    
    return a + b + c + d