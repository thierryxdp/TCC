def pontos_por_time(jogo):
    '''
    list->dict'''
    
    nome_t1=jogo[0][0]
    nome_t2=jogo[0][1]
    goli=jogo[0][2]
    golv=jogo[1][2]
    
    if goli[0]>goli[1]:
        pontos_t1=3
        pontos_t2=0
    if goli[0]<goli[1]:
        pontos_t1=0
        pontos_t2=3
    if goli[0]==goli[1]:
        pontos_t1=1
        pontos_t2=1
        
  
    return {nome_t1:pontos_t1, nome_t2:pontos_t2}