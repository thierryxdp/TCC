def pontos_por_time(L1):
    """Calculo a pontuação de dois times, baseado em uma lista que contém
    as informações de duas partidas no formato 
    [[Time1,Time,[g1,g2]],[Time2,Time1,[g2,g1]]]. (List->Dic)"""
    
    Time1=str(L1[0][0])
    Time2=str(L1[0][1])
    if L1[0][2][0]>L1[0][2][1]:
        T1a=3 
        T2a=0
    elif L1[0][2][0]<L1[0][2][1]:
        T1a=0
        T2a=3
    else:
        T1a=1
        T2a=1
    if L1[1][2][0]<L1[1][2][1]:
        T1b=3 
        T2b=0
    elif L1[1][2][0]>L1[1][2][1]:
        T1b=0
        T2b=3
    else:
        T1b=1
        T2b=1 
        
    Total = {Time2:(T2a+T2b), Time1:(T1a+T1b)}
    return Total