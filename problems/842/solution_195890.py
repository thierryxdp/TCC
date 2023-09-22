#Start your python function here
def pontos_por_time(jogoi,jogov):
     
    nome_t1=jogoi[0]
    nome_t2=jogov[0]
    pontos_t1 = jogoi[2][0] + jogov[2][1]
    pontos_t2 = jogoi[2][1] + jogov[2][0]
    
    return {nome_t1:pontos_t1, nome_t2:pontos_t2}