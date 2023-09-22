def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    nf=str.replace(f,l,"#",(n-1))
    i=0
    while i<len(f):
        if l in nf:
        i=i+1
            return str.index(nf,l)
        else:
            return -1