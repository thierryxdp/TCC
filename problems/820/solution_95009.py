def posLetra(frase,letra,ocorrencia):
    pos=[]
    n=0
    while n <= len(frase):
        if frase[n]== letra:
            pos.append(n)
        n+=1
    if len(pos)>=ocorrencia:
        return(pos[ocorrencia-1])
    else:
        return(-1)