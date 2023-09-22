def posLetra(frase,letra,n):
    i=0
    u=3*letra
    p=''
    while i<len(frase) and p!=u:
        b=[str.index(frase,letra,i,len(frase)+1)]
        p=p+frase[b]
        i=i+1
    return b