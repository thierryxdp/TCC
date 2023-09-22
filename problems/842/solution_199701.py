def pontos_por_time (jogoida,jogovolta):
    jogoida=[time1,time2,[gc,gf]]
    jogovolta=[time2,time1,[gf,gc]]
    return { time1:jogoida[2][0]+jogovolta[2][1]
           time2: jogoida[2][1]+jogovolta[2][0]}