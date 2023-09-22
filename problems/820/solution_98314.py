def posLetra(frase,L,num):
    """..."""
    """..."""
    i = 0
    posicao = ()
    while i < len(frase):
        if frase[i] in L:
            return frase[i]