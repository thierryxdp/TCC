def posLetra(frase,a,o):
    b=0
    posi=0
    frase=list(frase)
    c=-1
    while b+1<o:
        list.remove(frase,a)
        posi=posi+1
        b=b+1
        c=list.index(frase,a)+posi
    return c