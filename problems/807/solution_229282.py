def conta_frases(texto):
    '''Função que retorna o número de frases que aparecem no 
texto de entrada;
    str -> int'''
    n=str.count(texto,'?')
    n+=str.count(texto,'!')
    n+=str.count(texto,'.')
    v=str.count(texto,'...')
    return n-2*v