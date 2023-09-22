def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    i=0
    while i<n:
        if f[i] in "aeiou":
            str.replace(f[i],"k")
        i=i+1
    return str.index(f,l)