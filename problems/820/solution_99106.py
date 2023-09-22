def posLetra(frase,letra,n):
    i=0
    u=n*letra
    p=''
    while i<len(frase):
        if letra==frase[i]:
            b=str.find(frase,letra,i,len(frase)+1)
            p=p+frase[b]
        i=i+1
    return b