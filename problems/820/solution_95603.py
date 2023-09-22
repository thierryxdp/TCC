def posLetra(frase, letra, ocorrencia):
    ''' Funcao que dada uma string e uma letra, retorna a posicação
    da letra de acordo com a ocorrencia desejada da letra, indicado
    por um numero inteiro como parametro (1 para primeira ocorrencia, 
    2 para segunda ocorrencia...). Em caso a menos ocorrencias do que 
    a desejada, a funcao retornará -1'''
    posicao = 0
    quantOcorrencia = 0
    quantLetras = len(frase)
    
    while posicao < quantLetras and quantOcorrencia != ocorrencia:
        if frase[posicao] ==letra:
            quantOcorrencia = quantOcorrencia+1
        if frase[posicao] == letra and quantOcorrencia != ocorrencia:
            posicao = posicao +1
            
        if frase[posicao] != letra or quantOcorrencia != ocorrencia:
            posicao = posicao + 1
            
        if quantOcorrencia == ocorrencia:
            return posicao         

    else:
        return -1