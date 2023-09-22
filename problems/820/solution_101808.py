def posLetra(frase,letra,n):
    repet=1
    i=0
    soma=0
    if n>str.count(frase,letra):
        soma=-1
    else:
        while repet<=n:
            str.find(frase[i:],letra)
            i=str.find(frase[i:],letra)
            soma+=i
            x+=1
    return soma