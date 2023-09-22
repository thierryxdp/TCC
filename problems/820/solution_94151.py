def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    if l in f:
            str.replace(f,l,"#",(n-1)) 
    return f