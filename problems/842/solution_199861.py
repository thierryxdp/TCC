def pontos_por_time(resultados):
    jogo1=resultados[0]
    jogo2=resultados[1]
    gols=jogo1[2]+jogo2[2]
    time1=jogo1[0]
    time2=jogo1[1]
    ponto1=0
    ponto2=0
    if gols[0]>gols[1]:
        ponto1=ponto1+3
    elif gols[1]>gols[0]:
        ponto2=ponto2+3  
        
    if gols[3]>gols[2]:
        ponto1=ponto1+3
    elif gols[2]>gols[3]:
        ponto2=ponto2+3
        
    if gols[0]==gols[1]:
        ponto1=ponto1+1
        ponto2=ponto2+1
    if gols[2]==gols[3]:
        ponto1=ponto1+1
        ponto2=ponto2+1
        
    dicionario={time1:ponto1,
                time2:ponto2}
    return dicionario