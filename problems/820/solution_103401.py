def posLetra(frase,letra,num):
    proximo = -1
    while proximo < len(frase):
        if proximo(frase) == letra:
            ocorrencia = ocorrencia + str.count(frase, letra)
        proximo = proximo + 1
    return ocorrencia