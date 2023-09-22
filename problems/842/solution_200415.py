def pontos_por_time(jogos):
    '''Retorna o número de pontos do time na fase'''
    '''list->string'''
    jogo1=jogos[0]
    jogo2=jogos[1]
    Cor1=jogo1[0]
    Fla1=jogo1[1]
    golCor1=(jogo1[2])[0]
    golFla1=(jogo1[2])[1]
    if jogo2[1]==Cor1:
        Cor2=Cor1
        Fla2=Fla1
    else:
        Cor2=jogo2[1]
        Fla2=jogo2[0]
    golCor2=(jogo2[2])[1]
    golFla2=(jogo2[2])[0]
    if golCor1==golFla1:
        pontoCor1=1
        pontoFla1=1
    if golCor1>golFla1:
        pontoCor1=3
        pontoFla1=0
    else:
        pontoCor1=0
        pontoFla1=3
    if golCor2==golFla2:
        pontoCor2=1
        pontoFla2=1
    if golCor2>golFla2:
        pontoCor2=3
        pontoFla2=0
    else:
        pontoCor2=0
        pontoFla2=3
    
    pontoFla=pontoFla1+pontoFla2
    pontoCor=pontoCor1+pontoCor2
    dicio={Fla1:pontoFla,Cor1:pontoCor}
    return dicio