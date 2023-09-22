def inverte(frase:str) -> str:
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto1 = frase.lower()
    texto2 = str.split(texto1, ' ')
    texto3 = str.split(texto2, if '-')
    texto4 = texto3
    return texto4