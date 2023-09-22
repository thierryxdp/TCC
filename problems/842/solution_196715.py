def pontos_por_time(lista1):
    """ função que retorna os pontos de um time em dois jogos no campeonato
    list => dicionário """
    timeA=(lista1[0])[0]
    timeB=(lista1[0])[1]
    jogo1=(lista1[0])[2]
    jogo2=(lista1[1])[2]
    if jogo1[0]==jogo1[1]:
        pontuacaoAA=1
        pontuacaoBA=1
    elif jogo1[0]>jogo1[1]:
        pontuacaoAA=3
    else:
        pontuacaoBA=0
        pontuacaoAA=0
        pontuacaoBA=3
    if jogo2[0]==jogo2[1]:
        pontuacaoAB=1
        pontuacaoBB=1
    elif jogo2[0]>jogo2[1]:
        pontuacaoAB=0
        pontuacaoBB=3
    else:
        pontuacaoAB=3
        pontuacaoBB=0
    
    return {timeA:(pontuacaoAA+pontuacaoAB),timeB:(pontuacaoBA+pontuacaoBB)}