def posLetra(frase,letra,n):
    x=1
    i=0
    if n>str.count(frase,letra):
        return -1
    else:
        while x<=n:
            str.find(frase[i:],letra)
            i=str.find(frase[i:],letra)
            x=x+1
    return i