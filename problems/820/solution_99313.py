def posLetra(frase,l):
    i=0
    r=(,)
    while i < len(frase):
        if l in frase[i]:
            r= r+(i,)
        i=i+1
    return r