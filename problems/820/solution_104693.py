def posLetra(string,letra,numero):
    ocorrencia=string.find(letra)
    while ocorrencia>=0 and numero>1:
        ocorrencia=string.find(letra,ocorrencia+1)
        numero-=1
    return ocorrencia