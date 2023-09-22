def posLetra(string,letra,numero):

#retorna em que posição da string uma letra informada esta, podendo ser informado qual ocorrencia da letra queremos    
    
    contador = 0
    posicoes = []


    while contador < len(string):
        if string[contador] == letra:
            list.append(posicoes, contador)
        contador += 1

    if numero > string.count(letra):
        return -1

    return posicoes[numero-1]