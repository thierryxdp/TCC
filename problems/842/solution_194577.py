def pontos_por_time(jogo):
    ''' recebe uma lista de dois elementos que são listas e retorna o nome do time
    e sua pontuação final que é o ponto por vitória mais o ponto por empate.
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
    if golv[0]>golv[1]:
        pontos_t2=pontos_t2+3
    if golv[0]<golv[1]:
        pontos_t1=pontos_t1+3
    if golv[0]==golv[1]:
        pontos_t1=pontos_t1+1
        pontos_t2=pontos_t2+1
  
    return {nome_t1:pontos_t1, nome_t2:pontos_t2}