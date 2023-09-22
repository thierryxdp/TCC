def inverte(frase):
    """funcaao que dada uma frase retorne uma outra frase que contenha
        as mesmas palavras da frase de entrada na ordem inversa."""
    lista = str.split(phrase)
    lista.reverse()
    #lista = list.reverse(lista)
    phrase = str.join(" ", lista)
    return frase