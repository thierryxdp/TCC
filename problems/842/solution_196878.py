def pontos_por_time(l):#os jogos possuem os mesmo 2 times
    l0=l[0]#primeiro jogo
    l1=l[1]#segundo jogo
    T0=l0[0]#primeiro time
    T1=l0[1]#segundo time
    P0=l0[2]#pontos no primeiro jogo
    P1=l1[2]#pontos no segundo jogo
    P00=P0[0]#pontos do primeiro time no primeiro jogo
    P01=P0[1]#pontos do segundo time no primeiro jogo
    P10=P1[0]#pontos do primeiro time no segundo jogo
    P11=P1[1]#pontos do segundo time no segundo jogo
    if P00>P01 and P10>P11:
        return {T0:6,T1:0}
    elif P00>P01 and P10<P11 or P00<P01 and P10>P11:
        return {T0:3,T1:3}
    elif P00>P01 and P10==P11:
        return {T0:4,T1:1}
    elif  P00<P01 and P10<P11:
        return {T0:0,T1:6}
    elif P00<P01 and P10==P11:
        return {T0:1,T1:4}
    else:
        return {T0:1,T1:1}