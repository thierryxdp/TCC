def pontos_por_time(jogo):
    '''Retorna um dicionario com o nome do time e a quantidade de pontos que ele possui
    list->dict'''
    
    jogoIda=jogo[0]
    jogoVolta=jogo[1]
    
    time1=jogoIda[0]
    time2=jogoIda[1]
    
    pontosT1=0
    pontosT2=0
    
    if jogoIda[2][0]==jogoIda[2][1]:
        pontosT1+=1
        pontosT2+=1
    elif jogoIda[2][0]>=jogoIda[2][1]:
        pontosT1+=3
    else:
        pontosT2+=3
        
    indiceT1=jogoVolta.index(time1)
    indiceT2=jogoVolta.index(time2)
        
    if jogoVolta[2][indiceT1]==jogoVolta[2][indiceT2]:
        pontosT1+=1
        pontosT2+=1
    elif jogoVolta[2][indiceT1]>=jogoVolta[2][indiceT2]:
        pontosT1+=3
    else:
        pontosT2+=3
        
    return {time1:pontosT1,time2:pontosT2}