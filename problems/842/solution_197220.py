def pontos_por_time(lista1):
    
    time1 = lista1[0][0]
    time2 = lista1[0][1]
    
    gol_time1_jogo1 = lista1[0][2][0]
    gol_time2_jogo1 = lista1[0][2][1]
    gol_time1_jogo2 = lista1[1][2][0]
    gol_time2_jogo2 = lista1[1][2][1]
    
    if gol_time1_jogo1 > gol_time2_jogo1:
        pont_time1_jogo1 = 3
        pont_time2_jogo1 = 0
        
    if gol_time1_jogo1 < gol_time2_jogo1:
        pont_time1_jogo1 = 0
        pont_time2_jogo1 = 3
    
    if gol_time1_jogo1 == gol_time2_jogo1:
        pont_time1_jogo1 = 1
        pont_time2_jogo1 = 1
    
    if gol_time1_jogo2 > gol_time2_jogo2:
        pont_time1_jogo2 = 3
        pont_time2_jogo2 = 0
        
    if gol_time1_jogo2 < gol_time2_jogo2:
        pont_time1_jogo2 = 0
        pont_time2_jogo2 = 3
    
    if gol_time1_jogo2 == gol_time2_jogo2:
        pont_time1_jogo2 = 1
        pont_time2_jogo2 = 1