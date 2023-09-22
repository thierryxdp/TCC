def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    nf=str.replace(f,l,"#",(n-1))
    while i<len(f):
        i=i+1
        if l in nf:
        else:
            return -1
   		return str.index(nf,l)