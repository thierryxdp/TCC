def pontos_por_time(lista):
    '''funcao que dada uma lista contendo outras listas:
       L1 e L2 informando o nome do time e o numero de 
       gols em dois jogos de futebol entre esses  dois 
       times, retorna um dicionario cujos mapeamentos 
       sao: <nome do time>-><numero total de pontos>.
       O numero total é dado por 3* numero de vitoria +
       1*o numero de empate
       lista->dicionario'''
    time1=lista[1][1]
    time3=lista[0][1][0]
    pontuacao1=lista[0][2][0]
    pontuacao2= lista[1][2][1]
    time2=lista[0][1]
    time4=lista[0][1][1]
    pontua1=lista[0][2][1]
    pontua2=lista[1][2][0]
    pontuatotal=0
    pontuacaototal=0
    if pontua1>pontuacao1:
        pontuatotal= pontuatotal + 3
    else:
            pontuacaototal= pontuacaototal + 3
    if pontua2>pontuacao2:
        pontuatotal= pontuatotal + 3
    else:
        pontuacaototal=pontuacaototal + 3
    if pontua1==pontuacao1:
        pontuatotal= pontuatotal + 1
    if pontua1== pontuacao1:
        pontuacaototal= pontuacaototal + 1

    return{time2:pontuatotal, time1:pontuacaototal}