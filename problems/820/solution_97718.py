def posLetra(frase,letra,ocorrencia):
    if frase.count(letra) < ocorrencia:
        return -1
    cont = 1
    posi = frase.index(letra)
    while cont < ocorrencia:
        posi = frase.index(letra, posi + 1)
        cont = cont + 1
    return posi