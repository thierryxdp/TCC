def posLetra(frase,letra,oc):
    i = 0
    ocorrencias =0
    while i < len(frase):
        if letra == frase[i]:
            ocorrencias +=1
        if ocorrencias = oc:
            return i
        i+=1
    return -1