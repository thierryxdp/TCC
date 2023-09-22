def inverte(x=""):
    '''função que dada uma frase retorna outra com as mesmas palavras sem letras maiusculas
    e sem a pontuação'''
    x=x.split(" ")
    return str(" ").join(x[::-1])