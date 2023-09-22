def pontos_por_time(jogoida,jogovolta):
    '''Funcão que calcula o total de pontos de uma fase dos times Cormengo e Flamínthias; list,list-->str'''
    t1=jogoida[0]
    t2=jogovolta[0]
    vencedorida_t1= jogoida[2][0]>jogoida[2][1]
    vencedorida_t2= jogoida[2][1]>jogoida[2][0]
    vencedorvolta_t2= jogovolta[2][1]>jogovolta[2][0]
    vencedorvolta_t1= jogovolta[2][0]>jogovolta[2][1]
    empate=jogoida[2][1]==jogoida[2][0] or jogovolta[2][0]==jogovolta[2][1]

    if vencedorida_t1 and vencedorvolta_t1:
        {t1:6,t2:0}
    elif vencedorida_t1 and vencedorvolta_t2:
       {t1:3,t2:3}
    elif vencedorida_t1 and empate:
       {t1:4,t2:1}
    elif vencedorida_t2 and vencedorida_t2:
       {t1:0,t2:6}
    elif vencedorida_t2 and vencedorvolta_t1:
       {t1:3,t2:3}
    elif vencedorida_t2 and empate:
       {t1:1,t2:4}
    elif empate and empate:
      {t1:1,t2:1}