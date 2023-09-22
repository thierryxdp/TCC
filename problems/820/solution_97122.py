def posLetra(frase,a,o):
    b=0
    posi=0
    frase=list(frase)
    while b<o:
        frase=list.remove(frase,a)
        posi=posi+1
        b=b+1
    return list.index(frase,a)+posi