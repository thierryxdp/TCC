def conta_frases (texto):
    '''dado uma frase, a funcao retorna a quantidade de frases no texto'''
    x = str.count(texto,'.') 
    y = str.count(texto,'!') 
    z = str.count(texto,'?') 
    w = str.count(texto,'...') 
    return x + y + z + w