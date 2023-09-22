def inverte(x=""):
    '''função que dada uma frase retorna outra com as mesmas palavras na ordem
    inversa, sem letras maiusculas e sem a pontuação'''
    x=retira_pontuacao(x)
    x=x.split(" ")
    return str(" ").join(x[::-1])