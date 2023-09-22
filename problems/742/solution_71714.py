def substitui(s,x,i):
    """
    s-->string
    x-->caractere
    i-->posicao onde estara o caractere """

    s[i]=x
    return str(s[0:i]+x+s[i:])