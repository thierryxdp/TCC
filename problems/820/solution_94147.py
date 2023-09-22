def posLetra(frase,letra,numero):
    f=frase
    l=letra
    n=numero
    i=0
    repeticao=''
    while i<len(f):
        if l in f:
            str.replace(f,l,"1",(n-1))
        i=i+1 
    return str.index(f,l)