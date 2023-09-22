def inverte(frase):
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto1 = frase.lower()
    texto2 = texto1.split(' ')
    texto3 = seq.reverse(texto2)
    return texto3