def pontos_por_time (jogoi,jogov):
    nome_t1=jogoi [0]
    nome_t2=jogov [0]
    gols_t1=jogoi[2][0] + jogov[2][1]
    gols_t2=jogoi[2][1] + jogov[2][0]    
    if (jogoi[2][0]>jogoi[2][1] or jogov[2][1]>jogov[2][0]):
        return gols_t1+3
    elif (jogoi[2][0]==jogoi[2][1] or jogov[2][1]==jogov[2][0]):
        return gols_t1+1;gols_t2+1
    else:
        return gols_t2+3  
         
    return {nome_t1:n_gols_t1, nome_t2:n_gols_t2}