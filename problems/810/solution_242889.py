def inverte(frase):
    """ funcao que dada uma frase retorne uma outra frase
       que contenha as mesmas palavras da frase de entrada 
       na ordem inversa """
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase