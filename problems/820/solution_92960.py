def posLetra(frase,letra,numero):
    ''' '''
    ocorrencia=['naoconta',]
    contador=0
    if numero>(len(ocorrencia)-1):
        return -1
    while contador < len(frase):
        if frase[contador] in letra:
            ocorrencia=ocorrencia+[str.index(frase,letra,contador)]
        contador= contador+1
    return ocorrencia[numero]