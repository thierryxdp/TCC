def pontos_por_time(L1,L2):
    Time1=str(L1[0])
    Time2=str(L2[0])
    G1=int(L1[2])+int(L2[3])
    G2=int(L1[3])+int(L2[2])
    Total = {Time1:G1, Time2:G2}
    return Total