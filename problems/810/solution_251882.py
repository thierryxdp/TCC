def inverte(frase):
    '''função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem pontuação e sem letras maiúsculas. str-->str'''
    lista = str.split(frase)
    lista.reverse()
    frase = "".join(lista)
    return frase