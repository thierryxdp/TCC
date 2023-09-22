def inverte(frase):
    '''Dado uma frase, remove a pontuação e letras maiusculas, e então inverte a ordem da mesma.str->str'''
    frase1=((((frase.replace('.','')).replace(',','')).replace('?','')).replace('!','')).replace('-',' ')
    frase2=frase1.split(' ')
    frase3=frase2[::-1]
    frase4=str.lower(str.join(' ', frase3))
    return frase4