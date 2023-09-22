def inverte(frase:str) -> str:
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto1 = frase.lower()
    texto2 = texto1.remove(' ')
    return texto2