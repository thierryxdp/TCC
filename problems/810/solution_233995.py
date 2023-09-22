def inverte(frase):
    """funcao que dada uma frase retorne uma outra frase que contenha
        as mesmas palavras da frase de entrada na ordem inversa, sem letra maiuscula e sem pontuaçao."""
    lista = str.split(frase)
    lista.reverse()
    #lista = list.reverse(lista)
    frase = str.join(" ",lista)
    return frase