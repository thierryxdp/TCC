def posLetra(frase,letra,numero):
    ''' '''
    ocorrencia=['naoconta',]
    contador=0
    while contador < len(frase):
        if frase[contador] in letra:
            ocorrencia=ocorrencia+[str.find(frase,letra,contador)]
        if numero>=len(ocorrencia):
            return -1
        contador= contador+1
    return ocorrencia[numero]