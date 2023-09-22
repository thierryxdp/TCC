def posLetra(frase,letra,numero):
    
    i=0
    ocorrencia=0
    while i< len(frase):
        if letra == frase[i]:
            ocorrencia+=1
            if ocorrencia == n:
                return i
        i+=1
    return -1