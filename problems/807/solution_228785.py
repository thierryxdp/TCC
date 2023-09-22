def conta_frase(texto):
    '''Retorna a quantidade de frases escritas no texto.'''
    '''texto->str'''
    texto_1 = str.split(texto,'.')
    texto_1 = str.split(texto,'...')
    texto_1 = str.split(texto,'!')
    texto_1 = str.split(texto,'?')
    
    retun len(texto_1)