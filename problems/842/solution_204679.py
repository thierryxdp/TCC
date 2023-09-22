def pontos_por_time(lista1):

    Jogo_Ida = lista1[0]
    Jogo_volta = lista1[1]
    
    Time1 = Jogo_Ida[0]
    Time2 = Jogo_Ida[1]
    Placar_Ida = Jogo_Ida[2]

    Placar_volta = Jogo_volta[2]

    Gols_Time1_Ida = Placar_Ida[0]
    Gols_Time2_Ida = Placar_Ida[1]
    Gols_Time2_volta = Placar_volta[0]
    Gols_Time1_volta = Placar_volta[1]

    Pontos_Time1 = 0
    Pontos_Time2 = 0
    
    if Gols_Time1_Ida > Gols_Time2_Ida:
        Pontos_Time1 = 3
    elif Gols_Time1_Ida < Gols_Time2_Ida:
        Pontos_Time2 = 3
    else:
        Pontos_Time1 = Pontos_Time1 + 1
        Pontos_Time2 = Pontos_Time2 + 1 


    if Gols_Time1_volta > Gols_Time2_volta:
        Pontos_Time1 = Pontos_Time1 + 3
    elif Gols_Time1_Ida < Gols_Time2_volta:
        Pontos_Time2 = Pontos_Time2 + 3
    else:
        Pontos_Time1 = Pontos_Time1 + 1
        Pontos_Time2 = Pontos_Time2 + 1
        
    return {Time2:Pontos_Time2,
            Time1:Pontos_Time1}