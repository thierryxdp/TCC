def inverte(frase):
    '''Dada uma frase retorna outra frase contendo as mesmas palavras da frase
    de entrada na ordem inversa.'''
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase