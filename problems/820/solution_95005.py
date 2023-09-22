def posLetra(frase,letra,ocorrencia):
    pos=[]
    for n in range(len(frase)):
        if frase[n]== letra:
            pos.append(n)
    if len(pos)>=ocorrencia:
        return(pos[ocorrencia-1])
    else:
        return(-1)