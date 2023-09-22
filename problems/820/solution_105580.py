def posLetra(frase, letra, nOcorrencia):
    """
    	Recebe um <frase> uma <letra> e <nOcorrencia>
        retorna a posição da letra conforme sua ordem
        de ocorrência.
        str, str, int --> int
    """
    quantidadeDeOcorrencia = str.count(frase, letra)
    contadorDeIndex = 0
    contadorDeOcorrencia = 0
    if quantidadeDeOcorrencia >= nOcorrencia:
        for l in frase:
            if l == letra:
                contadorDeOcorrencia += 1
            if contadorDeOcorrencia == nOcorrencia:
                index = str.index(frase, l, contadorDeIndex)
                return index
            contadorDeIndex += 1 
    else:
        return -1