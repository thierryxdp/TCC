def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    nf=str.replace(f,l,"#",(n-1))
    if n<str.index(nf,l):
        return str.index(nf,l)
    else:
        return -1