def inverte(frase):
    """função que dada uma frase, retorna uma outra frase contendo as mesmas palavras  da frase de entrada, mas na ordem  inversa
    string -> string"""
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)

    return frase