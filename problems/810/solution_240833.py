def inverte(frase:str) -> str:
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto = frase.lower()
    texto = texto.replace('.','').replace('!', '').replace('?', '').replace('-', ' ')
    texto1 = texto.split(' ')
    texto2 = texto1[::-1]
    return texto2