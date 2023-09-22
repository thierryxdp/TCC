def pontos_por_time(lista):
    """ Função que retorna os pontos de um time em dois jogos no campeonato
    list,list - dicionário """
    timeA=(lista[0])[0]
    timeB=(lista[0])[1]
    jogo1=(lista[0])[2]
    jogo2=(lista[1])[2]
    if jogo1[0]==jogo1[1]:
        pontuacaoAA=1
        pontuacaoBA=1
    elif jogo1[0]>jogo1[1]:
        pontuacaoAA=3
        pontuacaoBA=0
    else:
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