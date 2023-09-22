def pontos_por_time(lista):
    '''calcula e retorna a pontuação dos times em uma fase;
list->dict'''
    L1 = lista[0]
    L2 = lista[1]
    j_ida = L1[2]
    j_volta = L2[2]
    gols_Cor_ida = j_ida[0]
    gols_Cor_volta = j_volta[1]
    gols_Flam_ida = j_ida[1]
    gols_Flam_volta = j_volta[0]
    
    if gols_Cor_ida > gols_Flam_ida and gols_Cor_volta > gols_Flam_volta:
        return {'Cormengo':6,'Flaminthians':0}
    elif(gols_Cor_ida > gols_Flam_ida and gols_Cor_volta == gols_Flam_volta) or (gols_Cor_ida == gols_Flam_ida and gols_Cor_volta > gols_Flam_volta):
        return {'Cormengo':4,'Flaminthians':1}
    elif gols_Cor_ida < gols_Flam_ida and gols_Cor_volta < gols_Flam_volta:
        return {'Flaminthians':6,'Cormengo':0}
    else:
        return {'Flaminthians':4,'Cormengo':1}