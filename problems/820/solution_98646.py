def posLetra(frase,l,n):
    """ Função que, dados uma """
    frase=[]
    i = 0


    while i < len(frase):

        if frase[i] in l:
            frase = frase + l
        i=i + 1
    return frase.count(frase,n)