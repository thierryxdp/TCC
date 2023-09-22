def pontos_por_time(lista):
    '''calcula e retorna a pontuação dos times em uma fase;
list->dict'''
    L1 = lista[0]
    L2 = lista[1]
    j_ida = L1[2]
    j_volta = L2[2]
    gols_tim1_ida = j_ida[0]
    gols_tim1_volta = j_volta[1]
    gols_tim2_ida = j_ida[1]
    gols_tim2_volta = j_volta[0]
    time1 = L1[0]
    time2 = L2[0]
    
    if gols_tim1_ida > gols_tim2_ida and gols_tim1_volta > gols_tim2_volta:
        return {time1:6,time2:0}
    elif(gols_tim1_ida > gols_tim2_ida and gols_tim1_volta == gols_tim2_volta) or (gols_tim1_ida == gols_tim2_ida and gols_tim1_volta > gols_tim2_volta):
        return {time1:4,time2:1}
    elif gols_tim1_ida < gols_tim2_ida and gols_tim1_volta < gols_tim2_volta:
        return {time1:0,time2:6}
    elif (gols_Cor_ida < gols_Flam_ida and gols_Cor_volta == gols_Flam_volta) or (gols_Cor_ida == gols_Flam_ida and gols_Cor_volta < gols_Flam_volta):
        return {time1:1,time2:4}
    else:
        return {time1:3,time2:3}