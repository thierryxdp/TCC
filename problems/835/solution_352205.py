def melhor_volta(matriz):
    '''
    Abre duas listas vazias para os melhores tempos
    e melhores corredores. Varre a matriz inicial e
    procura o melhor tempo do corredor (x) e a corrida 
    do melhor tempo (y). Posteriormente adiciona esses
    valores em listas de melhores tempos e suas respec-
    tivas corridas.
    
    Pega o menor tempo e coloca na variável de melhor 
    tempo (MT); Pega a posição do melhor tempo para achar
    a melhor volta e insere em MV; Pega a posição do melhor
    corredor em função do melhor tempo e acha a melhor corrida.
	
    Feito isso, retorna a tupla com os valores pedidos
    e uma soma (+1) para fins de compensação do índice.    
    '''
    LT = []; LC = []
    for i in matriz:
        x = min(i) #1
        y = i.index(x) #9
        LT.append(x) 
        LC.append(y) 
        
    MT = min(LT); MV = LT.index(MT); MC = LC[MV] 
    return (MV +1, MT, MC +1)