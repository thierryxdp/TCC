def melhor_volta(matriz): #Entrada: Matriz (list) #Procura na matriz qual foi o corredor mais rápido, o seu melhor tempo, e sua melhor volta
    listadetempos = []
    for lista in matriz:
        menorvolta = min(lista)
        listadetempos.append(menorvolta)
    
    menortempo = min(listadetempos)
    corredor = listadetempos.index(menortempo)
    melhor_corrida = matriz[corredor]
    melhorvolta = melhor_corrida.index(menortempo)

    corredor +=1
    melhorvolta +=1
    
    return (corredor, menortempo, melhorvolta) #Tuple: (int, int ,int)