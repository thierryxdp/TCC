def posLetra(frase,a,o):
    b=0
    posi=0
    frase=list(frase)
    while b+1<o:
        list.remove(frase,a)
        posi=posi+1
        b=b+1
    if a in frase:
        return list.index(frase,a)+posi
    else:
        return-1