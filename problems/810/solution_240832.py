def inverte(frase:str) -> str:
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto = frase.lower()
    texto = texto.replace('.','').replace('!', '').replace('?', '').replace('-', ' ')
    texto1 = texto[::-1]
    return texto1