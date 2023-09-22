def inverte(frase):
    """função que dada uma frase, retorna uma outra frase contendo as mesmas palavras  da frase de entrada, mas na ordem  inversa
    string -> string"""
    frase1 = str.split(frase)
    return frase1.reverse()