def inverte(x):
    """funcao que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase
    de entrada na ordem inversa, sem letras maiusculas e sem pontuacao
    str->str"""
    x=str.replace(x, "!", " ")
    x=str.replace(x, ".", " ")
    x=str.replace(x, ";", " ")
    x=str.replace(x, ",", " ")
    x=str.replace(x, "?", " ")
    x=str.replace(x, "-", " ")
    x=str.replace(x, ":", " ")