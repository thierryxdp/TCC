def pontos(x):
    '''
    	A função recebe uma lista com sa informações de dois jogos de 
        futebol da seguinte forma [['Cormengo', 'Flamínthians', [1, 0]], 
        ['Flamínthians', 'Cormengo', [2, 2]]], ou seja, contendo os nomes
        dos times e número de gols de cada jogo. Com isso, a função
        analisa o resultado cada jogo (atribuindo 3 pontos ao time
        vitorioso, 0 para o derrotado e 1 para cada em caso de empate).
        Por fim, a função calcula a pontuação final de cada time e 
        resulta em um dicionário que relaciona o nome do time e sua 
        pontuação.
    '''
    time1=x[0][0]
    time2=x[0][1]
    if x[0][2][0]>x[0][2][1]:
        j1t1=3
        j1t2=0
    elif x[0][2][0]==x[0][2][1]:
        j1t1=1
        j1t2=2
    else:
        j1t1=0
        j1t2=3
    
    if x[1][2][0]>x[1][2][1]:
        j2t1=3
        j2t2=0
    elif x[1][2][0]=x[1][2][1]:
        j2t1=1
        j2t2=1
    else:
        j2t1=0
        j2t2=3
    
    a={time1:j1t1+j2t1,time2:j1t2+j2t2}
    return a