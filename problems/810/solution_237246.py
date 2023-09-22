def inverte(frase):
    """Funcao que dada uma frase retorna outra frase com as mesmas palavras da frase
    de entrada na ordem inverse, sem letras maiusculas e sem a pontuacao.
    str->str"""
    return str.punctuation(frase[::-1])