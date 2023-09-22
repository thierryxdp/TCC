def posLetra(frase, letra_desejada, ocorrencia):
    contagem = 0
    posicao = 0
    for letra in frase:
        if letra == letra_desejada:
            contagem += 1
        
        if contagem == ocorrencia:
            return posicao
        
        posicao += 1
        
    return -1