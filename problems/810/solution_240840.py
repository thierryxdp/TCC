def inverte(frase:str) -> str:
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto = frase.lower()
    texto = texto.replace('.','').replace('!', '').replace('?', '').replace('-', ' ')
    texto = texto.split(' ')
    texto = texto.join()
    texto = texto[::-1]
    return texto