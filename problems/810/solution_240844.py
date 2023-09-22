def inverte(texto):
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto = texto.lower()
    texto = texto.replace('.','').replace('!', '').replace('?', '').replace('-', ' ')
    texto = texto.split(' ')
    texto = texto[::-1]
    return texto