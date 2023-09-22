#Start your python function here
def pontos_por_timme(pontos_jogo):
    
    ida = pontos_jogo[0]
    volta = pontos_jogo[1]
    
    time1 = ida[0]
    time2 = ida[1]
    
    gf_ida = ida[2][1]
    gc_ida = ida[2][0]
    gf_volta = volta[2][0]
    gc_volta = volta[2][1]
    
    if(gc_ida > gf and (gc_folta > gf_volta)