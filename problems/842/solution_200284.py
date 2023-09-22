def pontos_por_time(jogoi,jogov):
    '''Retorna o numero total de pontos de cada time dadas duas listas dos jogos de ida e volta; list,list->dict'''
    nome_t1=jogoi[0]
    nome_t2=jogoi[1]
    pontos_t1= jogoi[2]+jogov[3]
    pontos_t2=jogoi[3]+jogov[2]
        
    return {nome_t1:pontos_t1, nome_t2:pontos_t2}