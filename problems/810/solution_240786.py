def inverte(frase):
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto1 = frase.lower()
    texto2 = texto1.split(' ')
    texto3 = texto2.reverse(texto2, all)
    return texto3