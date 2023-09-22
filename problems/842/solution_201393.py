def pontos_por_time(jogoida,golsI,jogovolta,golsV): 
    if golsI[0] > golsI[1] and golsV[0] < golsV[1] :
    return { str(jogoida[0] ): 6, str(jogoida[1]) : 0 }
    if golsI[0] < golsI[1] and golsV[0] > golsV[1]:
    return { str(jogoida[0] ): 0, str(jogoida[1]) : 6 }
    if golsI[0] > golsI[1] and golsV[0] > golsV[1] or golsI[0] < golsI[1] and golsV[0] < golsV[1]:  :
    return { str(jogoida[0] ): 3, str(jogoida[1]) : 3 }
    if golsI[0] == golsI[1] and golsV[0] == golsV[1] :
    return { str(jogoida[0] ): 2 , str(jogoida[1]) : 2 }
    if golsI[0] == golsI[1] and golsV[0] < golsV[1]  or golsI[0] > golsI[1] and golsV[0] == golsV[1] :
    return { str(jogoida[0] ): 4, str(jogoida[1]) : 1 }
    if golsI[0] == golsI[1] and golsV[0] > golsV[1]  or golsI[0] < golsI[1] and golsV[0] == golsV[1] :
    return { str(jogoida[0] ): 1, str(jogoida[1]) : 4 }