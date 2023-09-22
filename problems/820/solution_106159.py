def posLetra (frase, letra, nOcorrencia):
    """ função que recebe uma string, uma letra e o numero de occorência da letra
   		e retorna a posição da string da ocrrência da letra vai está.
        str, str, int --> int """
    
    quantOcorrencia = str.count(frase, letra)
    contadorIndex = 0
    contadorOcorrencia = 0
    if quantOcorrencia >= nOcorrencia:
        for m in frase:
            if m == letra:
                contadorOcorrencia += 1
            if contadorOcorrencia == nOcorrencia:
                index = str.index(frase, m, contadorOcorrencia)
                return index
            contadorIndex += 1
    return -1