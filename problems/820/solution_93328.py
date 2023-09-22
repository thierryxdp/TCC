def posLetra(frase,letra,ocorr):
    i=0
    frase=list(frase)
    posicoes=[]
    if frase.count(letra)<ocorr:
        return -1
    while i<= len(frase)-1:
        if frase[i]==letra:
            posicoes.append(i)
        i+=1
    return posicoes[(ocorr-1)]