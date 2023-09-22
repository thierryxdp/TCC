def cortaPalavra(frase, palavra, posicaoInicial, posicaoFinal):
    posicao = str.find(frase, palavra, posicaoInicial, posicaoFinal)
    if (posicao != -1): # Recursao para contar as ocorrencias
        return cortaPalavra(
            str.replace(frase, palavra, "", 1),
            palavra,
            posicaoInicial,
            posicaoFinal-len(palavra)
        )
    return frase