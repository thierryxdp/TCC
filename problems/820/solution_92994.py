def posLetra(frase,letra,ocorrencia):
    if letra in frase:
        x=str.find(frase,letra,0)
        vez=1

        while vez<ocorrencia:
            x=str.find(frase,letra,x+1)
            vez=vez+1

        return x

    else:
        return -1