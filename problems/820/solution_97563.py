def posLetra(frase, letra, ocorrencia):
    tamanhoFrase = len(frase)
    contador = 0
    i = 0
    while i != tamanhoFrase:
        if(frase[i] == letra):
            contador += 1
            if(contador == ocorrencia):
                return i
        i += 1
    return -1