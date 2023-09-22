def posLetra(frase,letra,ocorrencia):
    i=0
    batat=0
    if ocorrencia<batat:
        return -1
    while i<len(frase) and  batat<ocorrencia:
        if frase[i] == letra:
            batat = batat +1
        i=i+1
    if batat<ocorrencia:
         return batat+letra
    else:
         return i-1