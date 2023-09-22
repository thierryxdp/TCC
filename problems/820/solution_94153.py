def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    nf=str.replace(f,l,"#",(n-1))
    if l in f:
             return str.index(nf,l)