def melhor_volta(matriz):
    '''função programada para receber uma matriz 6x10,
       onde 6 corredores realizam cada um 10 voltas de kart,
       o retorna é dado por: corredor da melhor performance,
       em que tempo e em qual volta, respectivamente.
       [list-->tuple]'''
    
    menortempo = []
    
    for corredor in matriz:
        tempo = min(corredor)
        list.append(menortempo,tempo)
    
    melhortempo = min(menortempo)
    corredor = list.index(menortempo,melhortempo)+ 1
    volta = list.index(matriz[corredor-1],melhortempo)+1
    
    return (corredor,melhortempo,volta)