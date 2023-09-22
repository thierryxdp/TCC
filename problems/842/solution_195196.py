def pontos_por_time(infos):
    """funçao que, dada uma lista composta por outras duas listas com o nome de um time A, time B e o placar deles dois no jogo de ida(lista 1) e jogo de volta(lista2), retorna o numero do saldo de pontos de ambos, sendo que a vitoria conta 3 pontos e empate 1, derrota nao pontua
    list(list(str1,str2,list),list(str2,str1,list)--->dict"""
    golsA_jogo1=infos[0][2][0]
    golsB_jogo1=infos[0][2][1]
    golsA_jogo2=infos[1][2][1]
    golsB_jogo2=infos[1][2][0]
    A=str(infos[0][0])
    B=str(infos[0][1])
    situacao_times={}
    if (golsA_jogo1>golsB_jogo1)and(golsA_jogo2>golsB_jogo2):
        situacao_times[A]='6 pontos'
        situacao_times[B]='0 pontos'
    elif (golsA_jogo1==golsB_jogo1)and(golsA_jogo2==golsB_jogo2):
        situacao_times[A]='2 pontos'
        situacao_times[B]='2 pontos'
    elif (golsA_jogo1<golsB_jogo1)and(golsA_jogo2<golsB_jogo2):
        situacao_times[A]='0 pontos'
        situacao_times[B]='6 pontos'
    elif ((golsA_jogo1>golsB_jogo1)and(golsA_jogo2==golsB_jogo2)) or ((golsA_jogo1==golsB_jogo1)and(golsA_jogo2>golsB_jogo2)):
        situacao_times[A]='4 pontos'
        situacao_times[B]='1 ponto'
    elif ((golsA_jogo1>golsB_jogo1)and(golsA_jogo2<golsB_jogo2)) or ((golsA_jogo1<golsB_jogo1)and(golsA_jogo2>golsB_jogo2)):
        situacao_times[A]='3 pontos'
        situacao_times[B]='3 pontos'
    else:
        situacao_times[A]='1 ponto'
        situacao_times[B]='4 pontos'
    return situacao_times