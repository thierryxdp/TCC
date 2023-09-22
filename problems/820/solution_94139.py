def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    i=0
    repetição=''
    while i<len(f):
        if f[i] in "abcdefghijklmnopqrswyxzuç":
            repetição=repetição+f[i]
            str.replace(f,f[i],"#")
        i=i+1
    return repetição