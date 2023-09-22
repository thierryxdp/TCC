def inverte(texto):
    '''Inverte a frase, tira pontuação e maiúsculas'''
    texto = texto.replace('.','').replace('!', '').replace('?', '').replace('-', ' ').replace(',', '')
    texto = texto.lower()
    texto = texto.split(' ')
    
    texto = texto[::-1]
    texto = ' '.join(texto)
    
    return texto