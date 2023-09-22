def pontos_por_time ( RI, RV):
    #checa a quantidade de gols 
    gols1_time1 = RI [2][:1]

    gols1_time2 = RI [2][1:]
    
    gols2_time1 = RV [2][1:]

    gols2_time2 = RV [2][:1]


    if  gols1_time1 > gols1_time2 and gols_time1 > golstime2:

        return { RI[0]: 6 , RV[0]: 0}