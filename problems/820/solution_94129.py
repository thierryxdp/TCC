def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    i=0
    while i<n:
        if l in f:
            str.replace(f,str.index(f,l),"0")
        i=i+1
    return str.index(f,l)