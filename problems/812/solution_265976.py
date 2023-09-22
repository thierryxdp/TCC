def retira_pontuacao(x):
    '''funcao que dada uma frase,
    retorne essa mesma frase,sem
    os caracteres de pontuação'''
    x=x.split("?")
    x=" ".join(x)
    x=x.split("!")
    x=" ".join(x)
    x=x.split("_")
    x=" ".join(x)
    x=x.split(",")
    x=" ".join(x)
    x=x.split("-")
    x=" ".join(x)
    x=x.split(":")
    x=" ".join(x)
    x=x.split(";")
    x=" ".join(x)
    x=x.split(".")
    x=" ".join(x)
    return x