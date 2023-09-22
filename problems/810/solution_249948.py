def inverte(x=""):
    '''função que dada uma frase retorne outra com as mesmas palavras na
    ordem inversa, sem letras maiúsculas e sem pontuação'''
    x=x.split(" ")
    return str(" ").join(x[::-1])