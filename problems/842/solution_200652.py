def pontos_por_time(lista):
    ''' retorna o total de pontos de cada time dada uma lista dos jogos de ida e volta
    list -> dict'''
    #listaParte1=>['nomeTime1', 'nomeTime2', [golsTime1,golsTime2]]
    #listaParte2=>['nomeTime2', 'nomeTime1', [golsTime2,golsTime1]]

    #lista=[['Cormengo','Flamínthians', [1, 0]], ['Flamínthians', 'Cormengo', [2, 2]]]

    #informacoes nomes dos times
    time1=lista[0][0]
    time2=lista[0][1]
    
    #informacoes jogo 1
    j1t1=lista[0][2][0]
    j1t2=lista[0][2][1]
    
    #informacoes jogo 2
    j2t1=lista[1][2][1]
    j2t2=lista[1][2][0]
    
    # pontos jogo1
    if j1t1>j1t2: #vitoria time1
        pt1, pt2=3,0
    elif j1t1==j1t2: #empate
        pt1, pt2=1,1
    else: #vitoria time2
        pt1,pt2=0,3

    # pontos jogo2
    if j2t1>j2t2: #vitoria time1
        pt1+=3
    elif j2t1==j2t2: #empate
        pt1+=1
        pt2+=1
    else: #vitoria time2
        pt2+=3

    return {time1:pt1, time2:pt2}