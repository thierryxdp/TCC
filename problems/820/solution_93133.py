def posLetra(frase,letra,ocorrencia):
    i = 0
    if letra not in frase[:ocorrencia]:
        return -1