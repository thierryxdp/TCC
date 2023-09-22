def conta_frases(texto):
    
    '''Função que dada um texto, retorna a quantidade de frases desse texto. str -> int'''
    
    b = str.count(texto,'...')
    texto2 = str.replace(texto,'...','')
    a = str.count(texto2,'!') + str.count(texto2,'?') + str.count(texto2,'.')
    
    return (a + b)