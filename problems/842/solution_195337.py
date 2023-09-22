#Start your python function here
def pontos_por_time(lista):
    ida=lista[0]
    volta=lista[1]
    time1=ida[0]
    time2=ida[1]
    timev1=time2
    timev2=time1
    gol1=ida[2][0]
    gol2=ida[2][1]
    golv1=volta[2][0]
    golv2=volta[2][1]
    pontos_fase=[]

    if gol1>gol2:
        if golv1>golv2:
            pontos_fase={time1:3,
                         time2:3}

        elif golv1==golv2:
            pontos_fase={time1:4,
                         time2:1}
        else:
             pontos_fase={time1:6,
                          time2:0}

    if gol1==gol2:
        if golv1>golv2:
            pontos_fase={time1:1,
                         time2:4}
            
        elif golv1==golv2:
            pontos_fase={time1:2,
                         time2:2}
        else:
            pontos_fase={time1:4,
                         time2:1}
    if gol2>gol1:
        if golv1>golv2:
            pontos_fase={time1:0,
                         time2:6}
        elif golv1==golv2:
            pontos_fase={time1:1,
                         time2:4}
        else:
            pontos_fase={time1:3,
                         time2:3}
        
    return pontos_fasedef pontos(lista):
    ida=lista[0]
    volta=lista[1]
    time1=ida[0]
    time2=ida[1]
    timev1=time2
    timev2=time1
    gol1=ida[2][0]
    gol2=ida[2][1]
    golv1=volta[2][0]
    golv2=volta[2][1]
    pontos_fase=[]

    if gol1>gol2:
        if golv1>golv2:
            pontos_fase={time1:3,
                         time2:3}

        elif golv1==golv2:
            pontos_fase={time1:4,
                         time2:1}
        else:
             pontos_fase={time1:6,
                          time2:0}

    if gol1==gol2:
        if golv1>golv2:
            pontos_fase={time1:1,
                         time2:4}
            
        elif golv1==golv2:
            pontos_fase={time1:2,
                         time2:2}
        else:
            pontos_fase={time1:4,
                         time2:1}
    if gol2>gol1:
        if golv1>golv2:
            pontos_fase={time1:0,
                         time2:6}
        elif golv1==golv2:
            pontos_fase={time1:1,
                         time2:4}
        else:
            pontos_fase={time1:3,
                         time2:3}
        
    return pontos_fase