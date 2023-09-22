def inverte(frase:str) -> str:
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto1 = frase.lower()
    texto2 = texto2.replace('.','').replace('!', '').replace('?', '').replace('-', ' ')
    texto3 = texto2[::-1]
    return texto3