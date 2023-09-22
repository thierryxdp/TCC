def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    i=0
    repeticao=''
    while i<len(f):
        if f[i] in "abcdefghijklmnopqrswyxzuç":
            repeticao=repeticao+f[i]
            str.replace(f,f[i],"#")
        i=i+1
    return repeticao