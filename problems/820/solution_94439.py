def posLetra(frase,letra,ocorrencia):
    posicao = 0
    contador = 0
    while posicao < len(frase):
        if frase[posicao] == letra:
            contador += 1
            if contador == ocorrencia:
                return posicao
        posicao += 1
    return -1