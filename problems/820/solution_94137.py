def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    i=0
    while i<len(f):
        if f[i] in "abcdefghijklmnopqrswyxzuç":
            str.replace(f,f[i],"#")
        i=i+1
    return str.index(f,l)