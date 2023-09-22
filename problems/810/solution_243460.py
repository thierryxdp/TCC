def inverte(frase):
    """ funcao que dada uma frase retorne uma outra frase
       que contenha as mesmas palavras da frase de entrada 
       na ordem inversa """
    frase = frase.replace(",", " ")
    frase = frase.replace("-", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace("!", " ")
    frase.invert( )
    return frase