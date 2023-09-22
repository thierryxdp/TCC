def inverte(frase):
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto1:str = frase.lower()
    texto2:str = texto1.remove(' ')
    return texto2