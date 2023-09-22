def inverte(txt):
    """ funcao que dada uma frase retorne uma outra frase
       que contenha as mesmas palavras da frase de entrada 
       na ordem inversa """
    txt = "nossa, como eu gosto de chocolate"
    return ''.join(list(reversed(txt)))