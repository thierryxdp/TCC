def pontos_por_time(ls):
    """Assinatura: list -> dict
    computa os pontos dos time na fase representa"""
    t1=ls[0][0]
    t2=ls[1][0]
    ret = {}
    ret[t1]=0
    ret[t2]=0
    
    gols_t1 = ls[0][2][0]
    gols_t2 = ls[0][2][1]
    contabiliza(ret, t1, gols_t1, t2, gols_t2)
    
    gols_t1 = ls[1][2][1]
    gols_t2 = ls[1][2][0]
    contabiliza(ret, t1, gols_t1, t2, gols_t2)
    return ret