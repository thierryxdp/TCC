def inverte(frase):
    '''
    Funçao que dada uma frase retorne uma outra frase contendo
    as mesmas palavras da frase de entrada na ordem inversa.
    '''
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase