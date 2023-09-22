def pontos_por_time(lista):
    lista1=lista[0]
    lista2=lista[1]
    placar1=lista1[2]
    placar2=lista2[2]
    if placar1[0]>x2:
        jogo1t1=3 
    elif placar1[1]>placar1[0]:
             jogo1t2=3 
    elif placar1[0]=placar1[1]:
             jogo1t1=jogo1t2=1
        elif placar1[0]<placar1[1]:
             jogo1t1=0
        elif placar[1]<placar1[0]:
             jogo1t2=0
        elif placar2[0]>placar2[1]:
             jogo2t2=3            
        elif placar2[1]>placar2[0]:                 
             jogo2t1=3
        elif placar2[0]=placar2[1]:
             jogo2to=jogo2t1=1
        elif placar2[0]<placar2[1]:
             jogo2t2=0
        elif placar2[1]<placar2[0]:
             jogo2t1=0            
            return: {time1:jogo1t1+jogo2t1,time2:jogo1t2+jogo2t2}