def posLetra(frase,letra,n):
    i=0
    u=3*letra
    p=''
    while i<len(frase) and p!=u:
        p=p+frase[str.index(frase,letra,i,len(frase)+1)]
        i=i+1
    return