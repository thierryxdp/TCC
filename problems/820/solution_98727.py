def posLetra(frase,letra,n):
    i=0
    u=3*letra
    p=''
    while i<len(frase) and p!=u:
        if letra==frase[i]:
            b=str.find(frase,letra,i,len(frase)+1)
            p=p+frase[b]
        else letra not in frase:
            return -1
        i=i+1
    return b