def conta_frases(frase):
    """ """
    frases= str.count(frase,"!") + str.count(frase,"?") +str.count(frase,".") - 2* str.count(frase,"...")
    return frases