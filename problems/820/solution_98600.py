def posLetra(frase,letra,numero):
    'dado uma frase, uma letra e um numero retirba en qye posição da frase aquela ocorrencia da letra esta'
    contador=0
    posicao=0
    while contador<numero:
        if frase[posicao] == letra:
            contador+=1
        posicao+=1
        if posicao==len(frase):
            return -1
    return posicao - 1