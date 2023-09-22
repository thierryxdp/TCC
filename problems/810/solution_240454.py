def inverte(frase):
    '''função que retorna o inverso de uma frase dada, contendo
        as mesmas palavras da frase de entrada na ordem inversa.'''
    lista = str.split(frase)
    lista[::-1]
    frase = str.join(" ", lista)
    return frase