def pontos_por_time(jogos):
    jogo1=jogos[0]
    jogo2=jogos[1]
    placar1=jogo1[2]
    placar2=jogo2[2]
    if placar1[0]>placar1[1]:
     Iponto1=3
    if placar1[0]<placar1[1]:
     Iponto2=3
    if placar1[0]==placar1[1]:
     Iponto1=Ipontos2=1
    if placar2[0]>placar2[1]:
     Vponto1=3
    if placar2[0]<placar2[1]:
     Vponto2=3
    if placar2[0]==placar2[1]:
     Vponto1=Vponto=1
     return[Iponto1+Vponto1,Iponto2+Vponto2]