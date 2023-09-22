def melhor_volta(placar):
    
    '''Função que dada uma matriz informando o tempo
    dos corredores, retorna quem foi que deu a melhor volta,
    em quanto tempo e em qual volta.
    
    :param placar:list
    :return:'''

    melhores = (0,float('inf'),0)
    linha=len(placar)
    coluna=len(placar[0])

    for i in range(linha):
        for j in range(coluna):
            if placar[i][j]<melhores[1]:
       		    melhores = (i+1,placar[i][j],j+1)

  	return melhores