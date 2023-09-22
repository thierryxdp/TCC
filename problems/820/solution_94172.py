def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    nf=str.replace(f,l,"#",(n-1))
    while i<len(f):
        if l in nf:
            return str.index(nf,l)
        else:
            return -1